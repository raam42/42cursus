#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/16 19:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/16 19:00:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class TemperatureError(GardenError):
    """Raised when temperature readings are biologically invalid."""
    pass


class SensorError(GardenError):
    """Raised when a hardware sensor fails to provide data."""
    pass


def validate_garden_sensor(data: str) -> int:
    """Processes sensor data and raises custom exceptions."""
    if not data:
        raise SensorError("Sensor output is empty (hardware failure)")
    
    temp = int(data)
    if temp < 0 or temp > 40:
        raise TemperatureError(f"Temp {temp}°C outside of safe growth range")
    
    return temp


def test_custom_errors() -> None:
    """Validates the custom pipeline handling."""
    test_inputs = ["25", "-10", "", "50"]

    for val in test_inputs:
        print(f"Testing input: '{val}'")
        try:
            result = validate_garden_sensor(val)
            print(f"Result: {result}°C [OK]")
        except TemperatureError as e:
            print(f"Custom Temperature Alert: {e}")
        except SensorError as e:
            print(f"Custom Hardware Alert: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        print()


if __name__ == "__main__":
    print("=== Garden Custom Error Pipeline ===\n")
    test_custom_errors()