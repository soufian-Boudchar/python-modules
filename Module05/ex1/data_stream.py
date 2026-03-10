from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass


    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        pass


    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
       super().__init__(stream_id)
       self.stream_type = "Environmental Data"
    
    def process_batch(self, data_batch: List[Any]) -> str:
        temp = []
        proc = data_batch.__len__()
        
        for item in data_batch:
            if isinstance(item, str):
                if item.startswith("temp:"):
                    try:
                        temp_val = float(item.split(":")[1])
                        temp.append(temp_val)
                    except ValueError:
                        raise ValueError
        if temp:
            avg_temp = sum(temp) / temp.__len__()
        else:
            avg_temp = 0.0

        return f"Sensor analysis: {proc} readings processed, avg temp: {avg_temp}°C"
    
class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        pass
    
    def process_batch(self, data_batch: List[Any]) -> str:
        proc = data_batch.__len__()
        


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"
    
    def process_batch(self, data_batch: List[Any]) -> str:
        pass



def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    #Sensor Stream
    try:
        sensor = SensorStream("SENSOR_001")
        sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
        processed_data = sensor.process_batch(sensor_data)
        print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
        formatted_data = ", ".join(sensor_data)
        print(f"Processing sensor batch: [{formatted_data}]")
        print(processed_data)
    except:
        print("invalid data")

    
    # Transaction Stream
    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    trans_data = ["buy:100", "sell:150", "buy:75"]
    processed_data = trans.process_batch(trans_data)
if __name__ == "__main__":
    main()



