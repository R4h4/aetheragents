from typing import TypeVar, Generic

from .agent import Agent
from .processor import Processor
from ..outputs import OutputHandler


T = TypeVar("T")


class AgentBuilder(Generic[T]):
    def __init__(self) -> None:
        self.processor: Processor | None = None
        self.output_handler: OutputHandler[T] | None = None
        self.input_type: str | None = None

    def set_processor(self, processor: Processor) -> "AgentBuilder[T]":
        self.processor = processor
        return self

    def set_output_handler(self, output_handler: OutputHandler[T]) -> "AgentBuilder[T]":
        self.output_handler = output_handler
        return self

    def set_input_type(self, input_type: str) -> "AgentBuilder[T]":
        self.input_type = input_type
        return self

    def build(self) -> Agent[T]:
        if not self.processor or not self.output_handler:
            raise ValueError("Processor and output handler must be set")
        return Agent[T](self.processor, self.output_handler)
