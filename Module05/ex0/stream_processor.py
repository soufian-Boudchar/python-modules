from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        #data processed:
        proc = 0
        for _ in data:
            proc += 1

        #calcul sum:
        total = 0
        for i in data:
            total += i

        avg = total / proc

        return f"Processed {proc} numeric values, sum={total}, avg={avg:.1f}"

    def validate(self, data: Any) -> bool:
        return data.__class__.__name__ == "list"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        chars = 0
        for _ in data:
            chars += 1

        words = 0
        in_word = False
        for c in data:
            if c != " " and not in_word:
                words += 1
                in_word = True
            elif c == " " and in_word:
                in_word = False

        return f"Processed text: {chars} characters, {words} words"

    def validate(self, data: Any) -> bool:
        return data.__class__.__name__ == "str"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        return data
    
    def validate(self, data: Any) -> bool:
        return (
            data.__class__.__name__ == "str"
                and data.startswith("ERROR:")
                    or data.startswith("INFO:")
        )

    def format_output(self, result: str) -> str:
        if result.startswith("ERROR:"):
            return f"[ALERT] ERROR level detected: {result[6:]}"
        elif result.startswith("INFO:"):
            return f"[INFO] INFO level detected: {result[5:]}"
        else:
            return ""

def main() -> None:
    # Numeric Processor:
    num_data = [1, 2, 3, 4, 5]
    num_proc = NumericProcessor()
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    print(f"Processing data: {num_data}")
    if num_proc.validate(num_data):
        print(f"Validation: Numeric data verified")
        print(f"{num_proc.format_output(num_proc.process(num_data))}")
    else:
        print("Error: Invalid data")

    print()

    # Text Processor
    text_data = "Hello Nexus World"
    text_proc = TextProcessor()

    print("Initializing Text Processor...")
    print(f"Processing data: \"{text_data}\"")
    if text_proc.validate(text_data):
        print(f"Validation: Text data verified")
        print(
            f"{text_proc.format_output(text_proc.process(text_data))}")
    else:
        print("Error: Invalid data")

    print()

    # Log Processor:
    log_proc = LogProcessor()
    log_data = "ERROR:"

    print("Initializing Log Processor...")
    print(f"Processing data: \"{log_data}\"")
    
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        print(f"Output: {log_proc.format_output(log_proc.process(log_data))}")
    else:
        print("Error: Invalid data")

    # polymorphic processing:
    
    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    
    processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data_stream: List[Any] = [[1, 2, 3], "Nexus Data", " System ready"]
    
if __name__ == "__main__":
    main()
