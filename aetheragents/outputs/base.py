from typing import Protocol, TypeVar, Any, runtime_checkable

T = TypeVar('T')


@runtime_checkable
class OutputHandler(Protocol[T]):
    """
    A protocol defining the interface for output processors.
    """

    def handle(self, raw_result: str, **kwargs: Any) -> T:
        """
        Process the raw result string and return the processed output.

        :param raw_result: The raw string result to be processed
        :param kwargs: Additional keyword arguments for processing options
        :return: The processed result of type T
        """
        ...
