from typing import Type

from .core.agent import Agent
from .core.builder import AgentBuilder
from .outputs.function_call_output import FunctionCallOutput
from .outputs.json_output import JSONOutput, T as ModelGeneric
from .outputs.text_output import TextOutput
from .processors import OpenAIProcessor, InputType


class AgentFactory:
    @staticmethod
    def create_json_agent(
        prompt: str,
        output_model: Type[ModelGeneric],
        model: str,
        system_prompt: str = None,
        base_url: str = None,
        api_key: str = None,
        input_type: str = InputType.TEXT,
    ) -> Agent:

        json_schema = output_model.model_json_schema()
        processor = OpenAIProcessor(
            model=model,
            prompt=prompt,
            system_prompt=system_prompt,
            api_key=api_key,
            base_url=base_url,
            output_schema=json_schema,
        )
        output_handler = JSONOutput(output_model)
        return (
            AgentBuilder()
            .set_processor(processor)
            .set_output_handler(output_handler)
            .set_input_type(input_type)
            .build()
        )

    @staticmethod
    def create_text_agent(
        prompt: str,
        system_prompt: str = None,
        api_key: str = None,
        base_url: str = None,
        model: str = None,
        input_type: str = InputType.TEXT,
    ):
        processor = OpenAIProcessor(
            model=model,
            prompt=prompt,
            system_prompt=system_prompt,
            api_key=api_key,
            base_url=base_url,
        )
        return (
            AgentBuilder()
            .set_processor(processor)
            .set_output_handler(TextOutput())
            .set_input_type(input_type)
            .build()
        )

    @staticmethod
    def create_function_call_agent(
        prompt: str,
        system_prompt: str = None,
        api_key: str = None,
        base_url: str = None,
        model: str = None,
        input_type: str = InputType.TEXT,
    ):
        processor = OpenAIProcessor(
            model=model,
            prompt=prompt,
            system_prompt=system_prompt,
            api_key=api_key,
            base_url=base_url,
        )
        return (
            AgentBuilder()
            .set_processor(processor)
            .set_output_handler(FunctionCallOutput())
            .set_input_type(input_type)
            .build()
        )

    @staticmethod
    def create_vision_agent(
        prompt: str,
        output_model: Type[ModelGeneric],
        system_prompt: str = None,
        base_url: str = None,
        api_key: str = None,
        model: str = None,
    ):
        return AgentFactory.create_json_agent(
            prompt,
            output_model,
            system_prompt,
            base_url,
            api_key,
            model,
            InputType.IMAGE,
        )
