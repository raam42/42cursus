#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_finally_block.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/16 20:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/16 20:00:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class PlantError(Exception):
    """Custom error for invalid plant watering operations."""
    pass


def open_watering_system() -> None:
    print(" Opening watering system")


def close_watering_system() -> None:
    print(" Closing watering system")


def water_plant(plant: str) -> None:
    """Waters a plant, or raises PlantError if invalid."""
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    if plant.capitalize() not in valid_plants:
        raise PlantError(f"Invalid plant name to water: '{plant.lower()}'")
    print(f" Watering {plant.capitalize()}: [OK]")


def test_watering_pipeline(plants: list[str]) -> None:
    """Pipeline demonstrating that 'finally' ensures resource cleanup."""
    open_watering_system()
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"\nCaught PlantError: {e}")
        print("\nending tests and returning to main")
    finally:
        # This will execute no matter what happens in the try block
        close_watering_system()


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    
    print("Testing valid plants...")
    test_watering_pipeline(["Tomato", "Lettuce"])
    
    print("\nTesting invalid plants...")
    test_watering_pipeline(["Tomato", "lettuce"])
    
    print("\nCleanup always happens, even with errors!")