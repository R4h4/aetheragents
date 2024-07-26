from typing import Type, TypeVar, Optional, Any, cast

from pydantic import BaseModel

from .core.agent import Agent
from .core.builder import AgentBuilder
from .outputs.function_call_output import FunctionCallOutput
from .outputs.json_output import JSONOutput
from .outputs.text_output import TextOutput
from .outputs import OutputHandler
from .processors import OpenAIProcessor, InputType

ModelGeneric = TypeVar("ModelGeneric", bound=BaseModel)


class AgentFactory:
    @staticmethod
    def create_json_agent(
        prompt: str,
        output_model: Type[ModelGeneric],
        model: str,
        system_prompt: Optional[str] = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        input_type: str = InputType.TEXT,
    ) -> Agent[ModelGeneric]:
        json_schema = output_model.model_json_schema()
        processor = OpenAIProcessor(
            model=model,
            prompt=prompt,
            system_prompt=system_prompt,
            api_key=api_key,
            base_url=base_url,
            output_schema=json_schema,
        )
        output_handler = cast(
            OutputHandler[ModelGeneric], JSONOutput[ModelGeneric](output_model)
        )
        return (
            AgentBuilder[ModelGeneric]()
            .set_processor(processor)
            .set_output_handler(output_handler)
            .set_input_type(input_type)
            .build()
        )

    @staticmethod
    def create_text_agent(
        prompt: str,
        model: str,
        system_prompt: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        input_type: str = InputType.TEXT,
    ) -> Agent[str]:
        processor = OpenAIProcessor(
            model=model,
            prompt=prompt,
            system_prompt=system_prompt,
            api_key=api_key,
            base_url=base_url,
        )
        return (
            AgentBuilder[str]()
            .set_processor(processor)
            .set_output_handler(TextOutput())
            .set_input_type(input_type)
            .build()
        )

    @staticmethod
    def create_function_call_agent(
        prompt: str,
        model: str,
        system_prompt: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        input_type: str = InputType.TEXT,
    ) -> Agent[dict[str, Any]]:
        processor = OpenAIProcessor(
            model=model,
            prompt=prompt,
            system_prompt=system_prompt,
            api_key=api_key,
            base_url=base_url,
        )
        output_handler = cast(OutputHandler[dict[str, Any]], FunctionCallOutput())
        return (
            AgentBuilder[dict[str, Any]]()
            .set_processor(processor)
            .set_output_handler(output_handler)
            .set_input_type(input_type)
            .build()
        )

    @staticmethod
    def create_vision_agent(
        prompt: str,
        output_model: Type[ModelGeneric],
        model: str,
        system_prompt: Optional[str] = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> Agent[ModelGeneric]:
        return AgentFactory.create_json_agent(
            prompt=prompt,
            output_model=output_model,
            system_prompt=system_prompt,
            base_url=base_url,
            api_key=api_key,
            model=model,
            input_type=InputType.IMAGE,
        )
