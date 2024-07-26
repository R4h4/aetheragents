from pydantic import BaseModel, ValidationError
from typing import Type, TypeVar, Generic, Dict, Any
import json

T = TypeVar("T", bound=BaseModel)


class InvalidJSONError(Exception):
    """Raised when the input is not valid JSON."""

    pass


class SchemaValidationError(Exception):
    """Raised when the JSON does not match the expected schema."""

    pass


class JSONOutput(Generic[T]):
    """
    A class for handling and processing json output.
    """

    def __init__(self, model: Type[T]):
        """
        Initialize the JSONOutput with a Pydantic model.

        :param model: A Pydantic model class
        """
        self.model = model

    def handle(self, raw_result: str) -> T:
        """
        Parse the raw JSON string and validate it against the model.

        :param raw_result: A JSON string
        :return: An instance of the Pydantic model
        :raises InvalidJSONError: If the input is not valid JSON
        :raises SchemaValidationError: If the JSON doesn't match the model schema
        """
        try:
            parsed_json = json.loads(raw_result)
        except json.JSONDecodeError as e:
            raise InvalidJSONError("Invalid JSON output") from e

        try:
            return self.model.model_validate(parsed_json)
        except ValidationError as e:
            raise SchemaValidationError(
                f"JSON does not match expected schema: {e}"
            ) from e

    def get_model_schema(self) -> Dict[str, Any]:
        """
        Get the JSON schema of the model.

        :return: A dictionary representing the JSON schema
        """
        return self.model.model_json_schema()

    def validate_json(self, raw_result: str) -> bool:
        """
        Validate JSON against the schema without creating a model instance.

        :param raw_result: A JSON string
        :return: True if valid, False otherwise
        """
        try:
            self.handle(raw_result)
            return True
        except (InvalidJSONError, SchemaValidationError):
            return False
