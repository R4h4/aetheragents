from typing import Any


class TextOutput:
    """
    A class for handling and processing text output.
    """

    def handle(self, raw_result: str, **kwargs: Any) -> str:
        """
        Process the input text by stripping whitespace and optionally removing extra whitespace.

        :param raw_result: The input text to process
        :param remove_extra_whitespace: Whether to remove extra whitespace between words
        :return: The processed text
        :raises ValueError: If the input is not a string
        """
        remove_extra_whitespace = kwargs.get("remove_extra_whitespace", True)

        if not isinstance(raw_result, str):
            raise ValueError("Input must be a string")

        processed_text = raw_result.strip()

        if remove_extra_whitespace:
            import re

            processed_text = re.sub(r"\s+", " ", processed_text)

        return processed_text
