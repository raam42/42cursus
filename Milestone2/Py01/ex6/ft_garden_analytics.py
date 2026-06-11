#!/bin/python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/27 20:05:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/05/27 20:05:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys


class Plant:
    """Generic base class encapsulating shared templates and validation."""

    BASE_H: float = 0.0
    BASE_A: int = 0
    GROWTH_RATE: float = 0.5

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()

        if height < 0:
            self._height = float(self.BASE_H)
        else:
            self._height = float(height)

        if age < 0:
            self._age = int(self.BASE_A)
        else:
            self._age = int(age)

    @classmethod
    def create_anonymous(cls) -> "Plant":
        """Class method acting as an alternative factory constructor."""
        return cls(
            name="Unknown plant",
            height=float(cls.BASE_H),
            age=int(cls.BASE_A)
        )

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def age_one_day(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height += self.GROWTH_RATE
        self._height = round(self._height, 1)

        if hasattr(self, "nutritional_value"):
            self.nutritional_value += 1


class Flower(Plant):
    """Flower subclass managing color profiles and blooming states."""

    BASE_H: float = 25.0
    BASE_A: int = 30
    GROWTH_RATE: float = 0.8

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.color: str = color
        self._is_blooming: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self._is_blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self._is_blooming = True


class Seed(Flower):
    """Operational Flower subclass designed specifically to track seeds."""

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age, color=color)
        self.seed_count: int = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds produced: {self.seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self.seed_count += 50


class Tree(Plant):
    """Tree subclass tracking trunk dimensions and shade profiles."""

    BASE_H: float = 200.0
    BASE_A: int = 365
    GROWTH_RATE: float = 2.5

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter: float = float(trunk_diameter)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )


class Vegetable(Plant):
    """Vegetable subclass tracking growth cycles and nutrition scaling."""

    BASE_H: float = 15.0
    BASE_A: int = 45
    GROWTH_RATE: float = 2.1

    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name=name, height=height, age=age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def process_single_plant(tokens: list[str]) -> None:
    """Parses token lists dynamically to instantiate and test subclasses."""
    species_type: str = tokens[0].capitalize()
    name: str = tokens[1]
    
    try:
        height: float = float(tokens[2])
        age: int = int(tokens[3])
    except Exception:
        print(f"Skipping line: Invalid numerical types for plant '{name}'")
        return

    plant: Plant

    if species_type == "Flower":
        if len(tokens) < 5:
            print("Error: Flower target row missing color attribute.")
            return
        plant = Seed(name, height, age, tokens[4])
        plant.show()
        plant.bloom()
        plant.bloom()
        plant.show()

    elif species_type == "Tree":
        if len(tokens) < 5:
            print("Error: Tree target row missing trunk diameter.")
            return
        try:
            diameter = float(tokens[4])
        except Exception:
            print("Error: Trunk diameter must be a float.")
            return
        plant = Tree(name, height, age, diameter)
        plant.show()
        plant.produce_shade()

    elif species_type == "Vegetable":
        if len(tokens) < 5:
            print("Error: Vegetable target row missing harvest season.")
            return
        plant = Vegetable(name, height, age, tokens[4])
        plant.show()
        print(f"[make {plant.name.lower()} grow and age for 20 days]")
        for _ in range(20):
            plant.grow()
            plant.age_one_day()
        plant.show()

    else:
        # Automatic creation fallback matching our core requirements
        plant = Plant.create_anonymous()
        plant.show()


def ft_garden_analytics() -> None:
    """Drives automated test parsing reading configuration input paths."""
    if len(sys.argv) != 2:
        print("Usage: python3 ft_plant_types.py [test_file.txt]")
        return

    filepath: str = sys.argv[1]
    print(f"=== Reading Data Suite from: {filepath} ===\n")

    try:
        with open(filepath, "r") as file:
            for line_num, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line or clean_line.startswith("#"):
                    continue

                tokens = clean_line.split(",")
                if len(tokens) < 4:
                    print(f"Line {line_num}: Corrupted layout formatting.")
                    continue

                print(f"--- Running Automated Test Case {line_num} ---")
                process_single_plant(tokens)
                print()
    except FileNotFoundError:
        print(f"Error: Target path file framework '{filepath}' not found.")


if __name__ == "__main__":
    ft_garden_analytics()
