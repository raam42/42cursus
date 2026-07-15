#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/14 22:15:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/14 22:15:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys


class Plant:
    """
    Generic base class encapsulating shared attributes, validation,
    and foundational growth mechanics.
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

    @classmethod
    def create_anonymous(cls) -> "Plant":
        """Class method acting as an alternative factory constructor."""
        return cls(name="Unknown plant", height=cls.BASE_H, age=cls.BASE_A)

    @staticmethod
    def is_under_a_year(age: int) -> bool:
        """Static validation utility checking if an age profile is < 365."""
        return age < 365

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = float(height)
        print(f"Height updated: {int(self._height)}cm")
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        self._age = int(age)
        print(f"Age updated: {int(self._age)} days")
        return True

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        """Master template method for increasing vertical height."""
        self._height += self._growth_rate
        self._height = round(self._height, 1)

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    """Flower subclass managing color profiles and blooming states."""

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._is_blooming: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not self._is_blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self._is_blooming = True


class Seed(Flower):
    """
    Operational multi-level subclass designed to track reproductive yields.
    """

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count: int = 0

    def show(self) -> None:
        """Extends Flower status output to include exact seed metrics."""
        super().show()
        print(f"Seeds: {self._seed_count}")

    def bloom(self) -> None:
        """Accumulates seeds upon a successful bloom cycle."""
        super().bloom()
        self._seed_count += 42


class Tree(Plant):
    """Tree subclass tracking trunk dimensions and shade profiles."""

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._growth_rate = 2.5
        self._trunk_diameter: float = float(trunk_diameter)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    """Vegetable subclass tracking growth cycles and nutrition scaling."""

    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._growth_rate = 2.1
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        """Extends the base grow method to simultaneously scale nutrition."""
        super().grow()
        self._nutritional_value += 1


def ft_plant_types() -> None:
    """Instantiates the specific types and triggers their unique behaviors."""
    print("=== Specialized Plant Types ===\n")
    
    # 1. Testing the Seed (Flower) multi-level inheritance
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    print("\n--- Displaying Sunflower State ---")
    sunflower.show()
    
    print("\n[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    print("\n--- Displaying Oak State ---")
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April")
    print("\n--- Displaying Tomato State ---")
    tomato.show()
    print("[make tomato grow]")
    tomato.grow()
    tomato.show()

    print("\n=== Anonymous Factory & Static Check")
    anon = Plant.create_anonymous()
    anon.show()
    is_young = Plant.is_under_a_year(anon.get_age())
    print(f"Is under a year old? {is_young}")


if __name__ == "__main__":
    ft_plant_types()
