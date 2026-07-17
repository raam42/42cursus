#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_different_errors.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/16 18:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/16 18:00:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def garden_operations(operation_number: int) -> None:
    """Performs operations that trigger specific error types."""
    if operation_number == 0:
        # ValueError: int() cannot parse letters
        int("abc")
    elif operation_number == 1:
        # ZeroDivisionError: self-explanatory
        _ = 10 / 0
    elif operation_number == 2:
        # FileNotFoundError: opening a non-existent path
        with open("/non/existent/file", "r") as f:
            f.read()
    elif operation_number == 3:
        # TypeError: mixing incompatible types
        _ = "string" + 5  # type: ignore


def test_error_types() -> None:
    """Demonstrates catching various exceptions in the pipeline."""
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        except Exception as e:
            print(f"Caught unexpected error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")