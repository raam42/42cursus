#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/16 17:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/16 17:00:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def input_temperature(temp_str: str) -> int:
    """Converts input to int and validates biological growth range (0-40°C)."""
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    """Runs the data validation pipeline against various sensor inputs."""
    test_cases = ["25", "abc", "100", "-50"]

    for data in test_cases:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        except Exception as e:
            print(f"Caught unexpected error: {e}")

    print("All tests completed program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()