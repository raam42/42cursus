#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/25 12:45:16 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/14 21:45:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys


class Plant:
    """
    Model representing a plant with encapsulated attributes and validation
    gates to secure its internal state against invalid modifications.
    """

    BASE_H: float = 0.0
    BASE_A: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self._growth_rate: float = 0.8

        # Validation for initial height
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print(f"Creation fallback: default height set to {self.BASE_H}cm")
            self._height = float(self.BASE_H)
        else:
            self._height = float(height)

        # Validation for initial age
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print(f"Creation fallback: default age set to {self.BASE_A} days")
            self._age = int(self.BASE_A)
        else:
            self._age = int(age)

        # Clean creation receipt
        print(f"Plant created: {self.name}: {self._height:.1f}cm, "
              f"{self._age} days old")

    def get_height(self) -> float:
        """Safely retrieves the protected height attribute."""
        return self._height

    def get_age(self) -> int:
        """Safely retrieves the protected age attribute."""
        return self._age

    def set_height(self, height: float) -> bool:
        """Validates and sets the plant height, rejecting negative inputs."""
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = float(height)
        print(f"Height updated: {int(self._height)}cm")
        return True

    def set_age(self, age: int) -> bool:
        """Validates and sets the plant age, rejecting negative inputs."""
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        self._age = int(age)
        print(f"Age updated: {int(self._age)} days")
        return True

    def show(self) -> None:
        """Displays the clean, standardized state of the plant."""
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def age(self) -> None:
        """Increases plant age chronologically by one day."""
        self._age += 1

    def grow(self) -> None:
        """Mutates height dynamically using the default rate."""
        self._height += self._growth_rate
        self._height = round(self._height, 1)


def ft_garden_security() -> None:
    """CLI driver testing the security boundaries of the Plant class."""
    if len(sys.argv) != 4:
        print("Usage: python3 ft_garden_security.py [name] [height] [age]")
        return

    plant_name: str = sys.argv[1]
    try:
        initial_height: float = float(sys.argv[2])
        initial_age: int = int(sys.argv[3])
    except Exception:
        print("Error: Height MUST be a float and Age MUST be an int.")
        return

    print("=== Garden Security System ===")
    plant = Plant(name=plant_name, height=initial_height, age=initial_age)

    print("\n--- Testing Rejection Check ---")
    new_h = plant.set_height(-22.5)
    new_a = plant.set_age(-9)
    if not new_h or not new_a:
        plant.show()


if __name__ == "__main__":
    ft_garden_security()
