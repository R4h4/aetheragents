import json
from typing import Dict, Set


class FunctionCallOutput:
    def handle(self, raw_result: str) -> Dict:
        try:
            function_call = json.loads(raw_result)
        except json.JSONDecodeError:
            raise ValueError("Invalid function call JSON")

        expected_keys = {"function", "arguments"}
        self.validate_output(function_call, expected_keys)

        return {
            "function": function_call["function"],
            "arguments": function_call["arguments"],
        }

    def validate_output(self, parsed_result: Dict, expected_keys: Set[str]):
        missing_keys = expected_keys - set(parsed_result.keys())
        if missing_keys:
            raise ValueError(
                f"Missing expected keys in output: {', '.join(missing_keys)}"
            )
