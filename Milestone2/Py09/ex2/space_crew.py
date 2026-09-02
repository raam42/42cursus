import json
import os
from datetime import datetime
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=50)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    def __str__(self) -> str:
        return (f"{self.name} ({self.rank.value}) - {self.specialization}")


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All members must be active for the mission")
        has_leader = any(
            member.rank in [Rank.COMMANDER, Rank.CAPTAIN] 
            for member in self.crew
        )
        if not has_leader:
            raise ValueError("Mission must have at least one"
                             " Commander or Captain")
        if self.duration_days > 365:
            experienced_crew = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if (experienced_crew / len(self.crew)) < 0.5:
                raise ValueError(
                    "Missions over 365 days require at least 50% of the cew"
                    " to have 5+ years experience"
                )
        return self


    def __str__(self) -> str:
        crew_roster = "\n ".join(str(member) for member in self.crew)
        return (
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew size: {len(self.crew)}\n"
            f"Crew members:\n {crew_roster}"
        )


def test_mission(data: dict[str, Any], test_name: str = "Batch Mission"
                 ) -> None:
    print(f"--- Running Test: {test_name} ---")
    try:
        mission = SpaceMission(**data)
        print("Valid mission created:\n"
              f"{mission}\n")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            if error['loc']:
                loc_path = " -> ".join(str(loc) for loc in error['loc'])
                print(f"- [{loc_path}]: {error['msg']}\n")
            else:
                print(f"- [Mission Rule]: {error['msg']}\n")
    print("=" * 42 + "\n")


def load_json_data(filepath: str) -> list[dict[str, Any]]:
    if not os.path.exists(filepath):
        print(f"[ERROR] Could not find '{filepath}'.\n"
              "Please run <<python3 .tools/data_exporter.py>> first.\n")
        return []
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def main() -> None:
    print("      Space Mission Crew Validation      \n",
          ("=" * 42 + "\n"))

    valid_file = 'generated_data/space_missions.json'
    valid_missions = load_json_data(valid_file)

    if valid_missions:
        for i, data in enumerate(valid_missions, start=1):
            test_mission(data, test_name=f"JSON Generated Mission #{i}")

    # 1. Define the raw data for individual crew members
    commander_sarah = {
        "member_id": "C001",
        "name": "Sarah Connor",
        "rank": "commander",
        "age": 45,
        "specialization": "Mission Command",
        "years_experience": 15,
        "is_active": True
    }
    lieutenant_john = {
        "member_id": "L002",
        "name": "John Smith",
        "rank": "lieutenant",
        "age": 32,
        "specialization": "Navigation",
        "years_experience": 6,
        "is_active": True
    }
    officer_alice = {
        "member_id": "O003",
        "name": "Alice Johnson",
        "rank": "officer",
        "age": 28,
        "specialization": "Engineering",
        "years_experience": 2,
        "is_active": True
    }
    inactive_captain = {
        "member_id": "C004",
        "name": "James Holden",
        "rank": "captain",
        "age": 35,
        "specialization": "Pilot",
        "years_experience": 10,
        "is_active": False
    }
    rookie_officer = {
        "member_id": "O005",
        "name": "Bob Rookie",
        "rank": "officer",
        "age": 22,
        "specialization": "Science",
        "years_experience": 1,
        "is_active": True
    }

    # 2. The Baseline: A perfectly valid mission[cite: 3]
    valid_mission = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2026-10-15T08:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        # Pydantic will automatically convert these dicts into CrewMember objects
        "crew": [commander_sarah, lieutenant_john, officer_alice]
    }

    # 3. Rule Violation: ID doesn't start with 'M'[cite: 3]
    invalid_id_mission = valid_mission.copy()
    invalid_id_mission["mission_id"] = "X2024_MARS"

    # 4. Rule Violation: Missing leadership[cite: 3]
    no_leader_mission = valid_mission.copy()
    no_leader_mission["crew"] = [lieutenant_john, officer_alice, rookie_officer]

    # 5. Rule Violation: Long mission with inexperienced crew[cite: 3]
    # 1 experienced (Sarah) + 2 rookies (Alice, Bob) = 33% (Fails the 50% rule)
    inexperienced_mission = valid_mission.copy()
    inexperienced_mission["crew"] = [commander_sarah, officer_alice, rookie_officer]

    # 6. Rule Violation: Inactive crew member assigned[cite: 3]
    inactive_mission = valid_mission.copy()
    inactive_mission["crew"] = [inactive_captain, lieutenant_john, officer_alice]

    # Bundle the tests in a dictionary
    test_suite = {
        "Mission ID Trap": invalid_id_mission,
        "No Leader Trap": no_leader_mission,
        "Experience Ratio Trap": inexperienced_mission,
        "Inactive Crew Trap": inactive_mission
    }


    # Execute the test suite
    for name, data in test_suite.items():
        test_mission(data, test_name=name)


if __name__ == "__main__":
    main()