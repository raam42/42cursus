#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    # Convert string to int, may raise ValueError
    return int(temp_str)

def test_temperature() -> None:
    # Test valid input
    try:
        val = input_temperature("25")
        print(f"Temperature is now {val}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    # Test invalid input
    try:
        val = input_temperature("abc")
        print(f"Temperature is now {val}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed program didn't crash!")

if __name__ == "__main__":
    print("Garden Temperature ===")
    test_temperature()