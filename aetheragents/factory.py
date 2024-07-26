from typing import Type, Set

from pydantic import BaseModel

from .core.builder import AgentBuilder
from .processors import OpenAIProcessor, InputType
from .outputs.json_output import JSONOutput, T as ModelGeneric
from .outputs.text_output import TextOutput
from .outputs.function_call_output import FunctionCallOutput
from config.settings import AI_DEFAULT_MODEL, AI_API_KEY, AI_ENDPOINT_URL


class AgentFactory:
    @staticmethod
    def create_json_agent(
            prompt: str, output_model: Type[ModelGeneric], system_prompt: str = None,
            base_url: str = None,
            api_key: str = None, model: str = None, input_type: str = InputType.TEXT
        ) -> ModelGeneric:
        api_key = api_key or AI_API_KEY
        model = model or AI_DEFAULT_MODEL
        base_url = base_url or AI_ENDPOINT_URL

        output_handler = JSONOutput[ModelGeneric](output_model)
        json_schema = output_model.model_json_schema()
        return (AgentBuilder()
                .set_processor(OpenAIProcessor(api_key, model, prompt, base_url, system_prompt, json_schema))
                .set_output_handler(output_handler)
                .set_input_type(input_type)
                .build())

    @staticmethod
    def create_text_agent(prompt: str, system_prompt: str = None, api_key: str = None,
                          base_url: str = None, model: str = None, input_type: str = InputType.TEXT):
        api_key = api_key or AI_API_KEY
        model = model or AI_DEFAULT_MODEL
        base_url = base_url or AI_ENDPOINT_URL

        return (AgentBuilder()
                .set_processor(OpenAIProcessor(api_key, model, prompt, base_url, system_prompt))
                .set_output_handler(TextOutput())
                .set_input_type(input_type)
                .build())

    @staticmethod
    def create_function_call_agent(
            prompt: str, system_prompt: str = None, api_key: str = None,
            base_url: str = None, model: str = None, input_type: str = InputType.TEXT
        ):
        api_key = api_key or AI_API_KEY
        model = model or AI_DEFAULT_MODEL
        base_url = base_url or AI_ENDPOINT_URL

        return (AgentBuilder()
                .set_processor(OpenAIProcessor(api_key, model, prompt, base_url, system_prompt))
                .set_output_handler(FunctionCallOutput())
                .set_input_type(input_type)
                .build())

    @staticmethod
    def create_vision_agent(
            prompt: str, output_model: Type[ModelGeneric], system_prompt: str = None,
            base_url: str = None, api_key: str = None, model: str = None):
        return AgentFactory.create_json_agent(
            prompt, output_model, system_prompt, base_url, api_key, model, InputType.IMAGE
        )
