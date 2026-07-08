#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/09 00:15:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/09 00:15:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Plant:
    """Generic base class encapsulating shared templates and validation."""

    BASE_H: float = 0.0
    BASE_A: int = 0
    GROWTH_RATE: float = 0.5

    class _Stats:
        """Nested class managing encapsulated lifecycle statistics."""
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self._stats = self._Stats()

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
        """Class method factory acting as an alternative constructor."""
        return cls(
            name="Unknown plant",
            height=float(cls.BASE_H),
            age=int(cls.BASE_A)
        )

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
        self._stats._show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def age(self) -> None:
        self._stats._age_calls += 1
        self._age += 1

    def grow(self) -> None:
        """Master structural Template Method utilizing class overrides."""
        self._stats._grow_calls += 1
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
        """Extends Flower status output to include exact seed metrics."""
        super().show()
        print(f"Seeds produced: {self.seed_count}")

    def bloom(self) -> None:
        """Accumulates 50 seeds on every single successive bloom call."""
        super().bloom()
        self.seed_count += 50


class Tree(Plant):
    """Tree subclass tracking trunk dimensions and shade profiles."""

    BASE_H: float = 200.0
    BASE_A: int = 365
    GROWTH_RATE: float = 2.5

    class _TreeStats(Plant._Stats):
        """Extended nested class to track Tree-specific behaviors."""
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter: float = float(trunk_diameter)
        # Overwrite the base stats object with the specialized Tree version
        self._stats = self._TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
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


def display_statistics(plant: Plant) -> None:
    """Unique standalone function to output encapsulated statistics."""
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


def run_garden_analytics(garden: list[Plant]) -> None:
    """Computes and prints statistical summaries of the garden collection."""
    if not garden:
        print("The garden is currently empty.")
        return

    print("=== Garden Analytics Reports ===")

    total_height = sum(p.get_height() for p in garden)
    avg_height = total_height / len(garden)
    print(f"Total plants tracked: {len(garden)}")
    print(f"Average garden height: {round(avg_height, 2)}cm")

    total_nutrition = sum(
        v.nutritional_value for v in garden if isinstance(v, Vegetable)
    )
    print(f"Total vegetable nutritional yield: {total_nutrition}")


def ft_garden_analytics() -> None:
    """Initializes a complete test garden list and performs a simple run."""
    print("=== Initializing All Subclasses Suite ===\n")

    garden_registry: list[Plant] = [
        Seed(name="sunflower", height=80.0, age=45, color="yellow"),
        Tree(name="oak", height=200.0, age=365, trunk_diameter=5.0),
        Vegetable(name="tomato", height=5.0, age=10, harvest_season="April"),
        Plant.create_anonymous()
    ]

    print("--- Baseline Population States ---")
    for plant in garden_registry:
        plant.show()
        print()

    print("[Simulating 20 days of unified garden growth]")
    for _ in range(20):
        for plant in garden_registry:
            plant.grow()
            plant.age()

    print("\n--- Triggering Class Specific Actions ---")
    for plant in garden_registry:
        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.produce_shade()

    print("\n--- Final Population States ---")
    for plant in garden_registry:
        plant.show()
        print()
        
    print("--- Object Lifecycle Statistics ---")
    for plant in garden_registry:
        display_statistics(plant)
        print()

    run_garden_analytics(garden_registry)


if __name__ == "__main__":
    ft_garden_analytics()
