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


def test_contact(data: dict[str, Any], test_name: str) -> None:
    print(f"--- Running test: {test_name} ---")
    try:
        contact = AlienContact(**data)
        print("Valid contact report:\n"
              f"{contact}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"- {error['msg']}")
    print("=" * 42 + "\n")


def main() -> None:
    print("      Alien Contact Log Validation      \n",
          ("=" * 38))
    valid_radio = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-09-01T23:00:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 3.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": True
    }

    invalid_id = valid_radio.copy()
    invalid_id["contact_id"] = "UFO_2024_001"

    invalid_physical = valid_radio.copy()
    invalid_physical.update({
        "contact_id": "AC_2024_002",
        "contact_type": "physical",
        "is_verified": False
    })

    invalid_telepathic = valid_radio.copy()
    invalid_telepathic.update({
        "contact_id": "AC_2024_003",
        "contact_type": "telepathic",
        "witness_count": 2
    })

    invalid_signal = valid_radio.copy()
    invalid_signal.update({
        "contact_id": "AC_2024_004",
        "signal_strength": 8.5,
        "message_received": None
    })

    test_suite = {
        "Happy Path": valid_radio,
        "ID Format Trap": invalid_id,
        "Physical Verification Trap": invalid_physical,
        "Telepathic Witness Trap": invalid_telepathic,
        "Strong Signal Trap": invalid_signal
    }

    for name, data in test_suite.items():
        test_contact(data, name)


if __name__ == "__main__":
    main()