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