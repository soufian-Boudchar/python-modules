from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceModel(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    try:
        st_1 = SpaceModel(station_id="ISS001",
                          name="International Space Station",
                          crew_size=6,
                          power_level=85.5,
                          oxygen_level=92.3,
                          is_operational=True,
                          last_maintenance=datetime(1999, 12, 12),
                          notes=None)
        print(f"ID: {st_1.station_id}")
        print(f"Name: {st_1.name}")
        print(f"Crew: {st_1.crew_size} people")
        print(f"Power: {st_1.power_level}%")
        print(f"Oxygen: {st_1.oxygen_level}%")
        status = 'Operational' if st_1.is_operational else 'Maintenance'
        print(f"Status: {status}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])

    print("\n========================================")
    print("Expected validation error:")

    try:
        st_1 = SpaceModel(station_id="ISS001",
                          name="International Space Station",
                          crew_size=9999,
                          power_level=85.5,
                          oxygen_level=92.3,
                          is_operational=True,
                          last_maintenance=datetime(1999, 12, 12),
                          notes=None)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR]: {e}")
