import re
from typing import Dict, Any, Set, List

import openai


class InputType:
    TEXT = "text"
    IMAGE = "image"


class OpenAIProcessor:
    def __init__(self, api_key: str, model: str, prompt: str, 
                 base_url: str = None, system_prompt: str = None,
                 output_schema: Dict[str, Any] = None, input_type: str = InputType.TEXT):
        self.model = model
        self.prompt = prompt
        self.system_prompt = system_prompt
        self.output_schema = output_schema
        self.input_type = input_type
        self.expected_keys = set(re.findall(r'\{(\w+)\}', prompt))
        if input_type == InputType.IMAGE:
            self.expected_keys.update('image')
        self.client = openai.OpenAI(
            base_url=base_url,
            api_key=api_key
        )

    def process(self, **kwargs: Any) -> str:
        self.validate_input(self.expected_keys, set(kwargs.keys()))

        messages = self._prepare_messages(kwargs)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={"type": "json_object"} if self.output_schema else None,
        )

        return response.choices[0].message.content

    def _prepare_messages(self, kwargs: Dict[str, Any]) -> List[Dict[str, Any]]:
        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})

        if self.input_type == InputType.TEXT:
            filled_prompt = self.prompt.format(**kwargs)
            messages.append({"role": "user", "content": filled_prompt})
        elif self.input_type == InputType.IMAGE:
            image_data = kwargs.get('image')
            if not image_data:
                raise ValueError("Image data is required for image input type")

            filled_prompt = self.prompt.format(**{k: v for k, v in kwargs.items() if k != 'image'})
            messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": filled_prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}"
                        }
                    }
                ]
            })

        if self.output_schema:
            messages.append({
                "role": "system",
                "content": f"Please provide your response in JSON format according to this schema: {self.output_schema}"
            })

        return messages

    def validate_input(self, expected_keys: Set[str], provided_keys: Set[str]) -> None:
        missing_keys = expected_keys - provided_keys
        if missing_keys:
            raise ValueError(f"Missing required arguments: {', '.join(missing_keys)}")

        extra_keys = provided_keys - expected_keys
        if extra_keys and 'image' not in extra_keys:
            raise ValueError(f"Unexpected arguments provided: {', '.join(extra_keys)}")