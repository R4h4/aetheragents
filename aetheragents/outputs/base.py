from typing import Any, Dict, Protocol, Set


class OutputHandler(Protocol):
    def handle(self, raw_result: Any) -> Any:
        ...

    def validate_output(self, parsed_result: Dict, expected_keys: Set[str]) -> None:
        ...
