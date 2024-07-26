from .agent import Agent
from .processor import Processor
from ..outputs import OutputHandler


class AgentBuilder:
    def __init__(self):
        self.processor = None
        self.output_handler = None
        self.input_type = None

    def set_processor(self, processor: Processor) -> 'AgentBuilder':
        self.processor = processor
        return self

    def set_output_handler(self, output_handler: OutputHandler) -> 'AgentBuilder':
        self.output_handler = output_handler
        return self

    def set_input_type(self, input_type: str) -> 'AgentBuilder':
        self.input_type = input_type
        return self

    def build(self) -> Agent:
        if not self.processor or not self.output_handler:
            raise ValueError("Processor and output handler must be set")
        self.processor.input_type = self.input_type
        return Agent(self.processor, self.output_handler)
