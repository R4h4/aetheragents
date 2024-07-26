from typing import Any, TypeVar, Generic
from .processor import Processor
from ..outputs import OutputHandler


T = TypeVar("T")


class Agent(Generic[T]):
    def __init__(self, processor: Processor, output_handler: OutputHandler[T]):
        self.processor = processor
        self.output_handler = output_handler

    def process(self, **kwargs: Any) -> T:
        raw_result = self.processor.process(**kwargs)
        return self.output_handler.handle(raw_result)
