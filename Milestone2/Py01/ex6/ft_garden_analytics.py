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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = int(age)
        return True

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def age_one_day(self) -> None:
        self._age += 1

    def grow(self) -> None:
        """Master Template Method utilizing class-level attribute constants."""
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


def run_garden_analytics(garden: list[Plant]) -> None:
    """Computes and prints statistical summaries of the garden collection."""
    if not garden:
        print("The garden is currently empty.")
        return

    print("=== Garden Analytics Reports ===")

    # 1. Average Height calculation across all plants
    total_height = sum(p.get_height() for p in garden)
    avg_height = total_height / len(garden)
    print(f"Total plants tracked: {len(garden)}")
    print(f"Average garden height: {round(avg_height, 2)}cm")

    # 2. Total Nutrition accumulation exclusively from Vegetables
    total_nutrition = sum(
        v.nutritional_value for v in garden if isinstance(v, Vegetable)
    )
    print(f"Total vegetable nutritional yield: {total_nutrition}")

    # 3. Collective Shade Reports triggered for all Trees
    print("\n--- Collective Canopy Shade Reports ---")
    for plant in garden:
        if isinstance(plant, Tree):
            plant.produce_shade()


def ft_garden_analytics() -> None:
    """Initializes a clean test garden list and performs a simple run."""
    print("=== Initializing Simple Garden Testing Suite ===")

    # Straightforward internal definitions containing exactly what the subject hints at
    garden_registry: list[Plant] = [
        Flower(name="rose", height=15.0, age=10, color="red"),
        Tree(name="oak", height=200.0, age=365, trunk_diameter=5.0),
        Vegetable(name="tomato", height=5.0, age=10, harvest_season="April")
    ]

    print("\n--- Baseline Population States ---")
    for plant in garden_registry:
        plant.show()
        print()

    # Simulate a 20-day natural jump across the entire population list
    print("[Simulating 20 days of unified garden growth]")
    for _ in range(20):
        for plant in garden_registry:
            plant.grow()
            plant.age_one_day()

    # Trigger custom actions manually on specific subclasses post-simulation
    print("\n--- Triggering Class Specific Actions ---")
    for plant in garden_registry:
        if isinstance(plant, Flower):
            plant.bloom()

    print("\n--- Final Population States ---")
    for plant in garden_registry:
        plant.show()
        print()

    # Execute analytics calculations pass
    run_garden_analytics(garden_registry)


if __name__ == "__main__":
    ft_garden_analytics()
