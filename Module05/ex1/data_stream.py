from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        res = [item for item in data_batch if criteria in str(item)]
        return res

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "status": "Active"
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        temp: List[float] = []
        proc = data_batch.__len__()

        for item in data_batch:
            if isinstance(item, str):
                if item.startswith("temp:"):
                    try:
                        temp_val = float(item.split(":")[1])
                        temp.append(temp_val)
                    except ValueError:
                        raise ValueError
            else:
                raise ValueError("invalid data!!")
        if temp:
            avg_temp = sum(temp) / temp.__len__()
        else:
            avg_temp = 0.0

        return (
            f"Sensor analysis: {proc} readings processed, "
            f"avg temp: {avg_temp}°C"
        )


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        proc = data_batch.__len__()
        hist = 0

        for item in data_batch:
            if isinstance(item, str):

                if item.startswith("buy:"):
                    hist += int(item.split(":")[1])

                elif item.startswith("sell:"):
                    hist -= int(item.split(":")[1])
            else:
                raise ValueError("Invalid data!!")

        return (
            f"Transaction analysis: {proc} operations, "
            f"net flow: {hist:+} units"
        )


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        errors = 0
        events = data_batch.__len__()

        for item in data_batch:
            if isinstance(item, str):
                if item == "error":
                    errors += 1
            else:
                raise ValueError("Invalid data!!")
        return (
            f"Event analysis: {events} events, "
            f"{errors} error detected"
        )


class StreamProcessor:

    def process_all(
        self, streams: List[DataStream], batches: List[List[Any]]
    ) -> None:
        print("Batch 1 Results:")

        try:
            for i in range(len(streams)):
                stream = streams[i]
                data = batches[i]

                result = stream.process_batch(data)

                print(f"- {result}")
        except ValueError as e:
            print(f"- ERROR: {e}")


def format_data(text: str, data: List[Any]) -> None:
    print(f"{text}: [", end="")
    print(*data, sep=", ", end="")
    print("]")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # Sensor Stream
    try:
        sensor = SensorStream("SENSOR_001")
        sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
        print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
        format_data("Processing sensor batch", sensor_data)
        print(sensor.process_batch(sensor_data))
    except ValueError as e:
        print(f"Sensor analysis: {e}")

    # Transaction Stream
    try:
        print("\nInitializing Transaction Stream...")
        trans = TransactionStream("TRANS_001")
        trans_data = ["buy:100", "sell:150", "buy:75"]
        print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
        format_data("Processing event batch", trans_data)
        print(trans.process_batch(trans_data))
    except ValueError as e:
        print(f"Transaction analysis: {e}")

    # Event Stream
    try:
        print("\nInitializing Event Stream...")
        event = EventStream("EVENT_001")
        event_data = ["login", "error", "logout"]
        print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
        format_data("Processing event batch", event_data)
        print(event.process_batch(event_data))
    except ValueError as e:
        print(f"Event analysis: {e}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    streams: List[DataStream] = [sensor, trans, event]
    data: List[List[Any]] = [["temp:1", "humidity:65"],
                             ["buy:10", "sell:15", "buy:75", "buy:199"],
                             ["login", "error", "logout"]]
    stream = StreamProcessor()
    stream.process_all(streams, data)

    try:
        print("\nStream filtering active: High-priority data only")
        sensor_data = ["CRITICAL: temp:99", "CRITICAL: pressure:2000"]
        filtered_sensor = sensor.filter_data(sensor_data, criteria="CRITICAL")
        trans_data = ["LARGE: tx:10000"]
        filtered_txs = trans.filter_data(trans_data, criteria="LARGE")
        print(
            f"Filtered results: {len(filtered_sensor)} "
            f"critical sensor alerts, {len(filtered_txs)} large transaction"
        )
        print("\nAll streams processed successfully. Nexus throughput optimal")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
