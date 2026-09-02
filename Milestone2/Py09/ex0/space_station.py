import json
import os
from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """
    Pydantic model representing space station telemetry data.
    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)

    def __str__(self) -> str:
        status = 'Operational' if self.is_operational else 'Offline'
        return (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Status: {status}"
        )


def test_station_build(data: dict[str, Any]) -> None:
    try:
        station = SpaceStation(**data)
        print("Valid station created:\n"
              f"{station}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"- Field '{error['loc'][0]}': {error['msg']}")
    print("=" * 42)


def load_json_data(filepath: str) -> list[dict[str, Any]]:
    if not os.path.exists(filepath):
        print(f"[ERROR] Could not find '{filepath}'.\n"
              "Please run <<python3 .tools/data_exporter.py>> first.\n")
        return []
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def main() -> None:
    print("         Space Station Data Validaton            \n"
          "===================================================")
    valid_file = 'generated_data/space_stations.json'
    invalid_file = 'generated_data/invalid_stations.json'

    valid_stations = load_json_data(valid_file)
    invalid_stations = load_json_data(invalid_file)

    if valid_stations:
        for data in valid_stations:
            test_station_build(data)
    if invalid_stations:
        for data in invalid_stations:
            test_station_build(data)


if __name__ == "__main__":
    main()