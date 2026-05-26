#!/bin/python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/25 12:45:16 by rodrigoa         #+#    #+#              #
#    Updated: 2026/05/25 12:45:16 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys

DEFAULT_BIOLOGY: dict[str, dict[str, float]] = {
        "Rose": {"height": 25.0, "age": 30.0},
        "Oak": {"height": 200.0, "age": 365.0},
        "Cactus": {"height": 5.0, "age": 90.0},
        "Sunflower": {"height": 80.0, "age": 45.0},
        "Fern": {"height": 15.0, "age": 120.0}
        }


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self._height: float = 0.0
        self._age: int = 0
        profile = DEFAULT_BIOLOGY.get(self.name, {"height": 0.0, "age": 0})
        default_h: float = float(profile["height"])
        default_a: int = int(profile["age"])

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print(f"Creation fallback: default height set to {default_h}cm")
            self._height = default_h
        else:
            self._height = float(height)
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print(f"Creation fallback: default age set to {default_a} days")
            self._age = default_a
        else:
            self._age = int(age)
        print(f"Plant created: {self.name}: {self._height}cm, "
              f"{self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        else:
            self._height = float(height)
            print(f"Height updated: {int(self._height)}cm")
            return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        else:
            self._age = int(age)
            print(f"Age updated: {int(self._age)} days")
            return True

    def show(self) -> None:
        print(f"Current state: {self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def age_one_day(self) -> None:
        self._age += 1

    def grow(self) -> None:
        if self.name == "Rose":
            self._height += 0.8
        elif self.name == "Sunflower":
            self._height += 2.5
        elif self.name == "Cactus":
            self._height += 0.1
        else:
            self._height += 0.5
        self._height = round(self._height, 1)


def ft_garden_security() -> None:
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
