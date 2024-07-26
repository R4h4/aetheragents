from typing import Any
from .processor import Processor
from ..outputs import OutputHandler


class Agent:
    def __init__(self, processor: Processor, output_handler: OutputHandler):
        self.processor = processor
        self.output_handler = output_handler

    def process(self, **kwargs: Any) -> Any:
        raw_result = self.processor.process(**kwargs)
        return self.output_handler.handle(raw_result)
