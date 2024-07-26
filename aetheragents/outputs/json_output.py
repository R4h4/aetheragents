import logging

from pydantic import BaseModel, ValidationError
from typing import Type, TypeVar, Generic
import json

# Define a TypeVar that is bound to BaseModel
T = TypeVar('T', bound=BaseModel)


class JSONOutput(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def handle(self, raw_result: str) -> T:
        try:
            # First, try to parse the raw result as JSON
            parsed_json = json.loads(raw_result)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON output")

        try:
            # Then, validate and create a Pydantic model instance
            return self.model.model_validate(parsed_json)
        except ValidationError as e:
            raise ValueError(f"JSON does not match expected schema: {e}")

    def get_json_schema(self) -> dict:
        return self.model.model_json_schema()
