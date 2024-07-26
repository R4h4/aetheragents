from typing import Any, Protocol, Set


class Processor(Protocol):
    def process(self, **kwargs: Any) -> str: ...

    def validate_input(self, provided_keys: Set[str]) -> None: ...
