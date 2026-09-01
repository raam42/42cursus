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
        print("Valid station created:\n",
              station)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])
    print("-" * 30)


def main() -> None:
    print("         Space Station Data Validaton            \n"
          "===================================================")
    test_cases = [
        {
            "station_id": "IS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2026-09-01T10:04:00",
            "is_operational": True,
            "notes": "Routine operations nominal."
        },
        {
            "station_id": "IS",
            "name": "Deep Space Nine",
            "crew_size": 25,
            "power_level": 105,
            "oxygen_level": 92.3,
            "last_maintenance": "2026-09-01T10:04:00"
        }
    ]
    for test in test_cases:
        test_station_build(test)


if __name__ == "__main__":
    main()