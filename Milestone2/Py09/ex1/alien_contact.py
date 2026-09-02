import json
import os
from datetime import datetime
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signal (>7.0) must include received message")
        return (self)

    def __str__(self) -> str:
        return(
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type.value}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: {repr(self.message_received)}\n"
        )


def test_contact(data: dict[str, Any]) -> None:
    try:
        contact = AlienContact(**data)
        print("Valid contact report:\n"
              f"{contact}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"- {error['msg']}\n")
    print("=" * 42 + "\n")


def load_json_data(filepath: str) -> list[dict[str, Any]]:
    if not os.path.exists(filepath):
        print(f"[ERROR] Could not find '{filepath}'.\n"
              "Please run <<python3 tools/py09_data_exporter.py>> first.\n")
        return []
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def main() -> None:
    print("      Alien Contact Log Validation      \n",
          ("=" * 38 + "\n"))

    valid_file = 'generated_data/alien_contacts.json'
    invalid_file = 'generated_data/invalid_contacts.json'

    valid_contacts = load_json_data(valid_file)
    invalid_contacts = load_json_data(invalid_file)

    if valid_contacts:
        for data in valid_contacts:
            test_contact(data)

    if invalid_contacts:
        for data in invalid_contacts:
            test_contact(data)


if __name__ == "__main__":
    main()