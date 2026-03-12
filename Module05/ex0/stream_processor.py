from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if data.__class__.__name__ in ("int", "float"):
            info = f"Processed 1 numeric values, sum={data}, avg=1"
            return super().format_output(info)

        proc = data.__len__()

        ttl = 0

        for i in data:
            ttl += i

        avg = ttl / proc

        info = f"Processed {proc} numeric values, sum={ttl:.2f}, avg={avg:.1f}"
        return super().format_output(info)

    def validate(self, data: Any) -> bool:
        if data.__class__.__name__ in ("int", "float"):
            return True

        elif data.__class__.__name__ == "list":
            for i in data:
                if i.__class__.__name__ not in ("int", "float"):
                    return False
        return True


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        chars = 0
        for _ in data:
            chars += 1
        words = data.split().__len__()
        info = f"Processed text: {chars} characters, {words} words"
        return super().format_output(info)

    def validate(self, data: Any) -> bool:
        return data.__class__.__name__ == "str"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        return data

    def validate(self, data: Any) -> bool:
        if data.__class__.__name__ != "str":
            return False
        return (data.startswith("ERROR:") or data.startswith("INFO:"))

    def format_output(self, result: str) -> str:
        if result.startswith("ERROR:"):
            return f"[ALERT] ERROR level detected:{result[6:]}"
        elif result.startswith("INFO:"):
            return f"[INFO] INFO level detected:{result[5:]}"
        else:
            return ""


def main() -> None:
    # Numeric Processor:
    try:
        num_data: Union[List[int], int] = [1, 2, 3, 4, 5]
        num_proc = NumericProcessor()
        print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

        print("Initializing Numeric Processor...")
        print(f"Processing data: {num_data}")
        if num_proc.validate(num_data):
            print("Validation: Numeric data verified")
            print(
                f"Output: {num_proc.format_output(num_proc.process(num_data))}"
            )
        else:
            raise ValueError("Invalid data")
    except ValueError as err:
        print("ERROR:", err)

    print()

    # Text Processor
    try:
        text_data = "Hello Nexus World"
        text_proc = TextProcessor()

        print("Initializing Text Processor...")
        print(f"Processing data: \"{text_data}\"")
        if text_proc.validate(text_data):
            print("Validation: Text data verified")
            print(
                f"Output: "
                f"{text_proc.format_output(text_proc.process(text_data))}"
            )
        else:
            raise ValueError("Invalid data")
    except ValueError as err:
        print("ERROR:", err)

    print()

    # Log Processor:
    try:
        log_proc = LogProcessor()
        log_data = "ERROR: Connection timeout"

        print("Initializing Log Processor...")
        print(f"Processing data: \"{log_data}\"")

        if log_proc.validate(log_data):
            print("Validation: Log entry verified")
            print(
                f"Output: {log_proc.format_output(log_proc.process(log_data))}"
            )
        else:
            raise ValueError("Invalid data")
    except ValueError as err:
        print("ERROR:", err)

    # polymorphic processing:

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(), LogProcessor()
    ]
    data_stream: List[Any] = [[1, 2, 3], "Nexus Data!!", "INFO:System ready"]

    i = 0
    for pr in processors:
        proc = pr
        print(
            f"Result {i + 1}: "
            f"{proc.format_output(proc.process(data_stream[i]))}"
        )
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
