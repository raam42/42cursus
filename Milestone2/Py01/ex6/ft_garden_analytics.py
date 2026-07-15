#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/15 22:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/15 22:00:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Plant:
    """Base class with encapsulated attributes and nested analytics."""
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

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name.capitalize()
        self._height: float = 0.0
        self._days: int = 0
        self._stats = self._Stats()  # Composition: Instance owns its stats

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print(f"Creation fallback: default height set to {self.BASE_H}cm")
            self._height = float(self.BASE_H)
        else:
            self._height = float(height)

        if days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print(f"Creation fallback: default age set to {self.BASE_A} days")
            self._days = int(self.BASE_A)
        else:
            self._days = int(days)

    @classmethod
    def create_anonymous(cls) -> "Plant":
        """Class method acting as an alternative factory constructor."""
        return cls(name="Unknown plant", height=cls.BASE_H, days=cls.BASE_A)

    @staticmethod
    def is_under_a_year(age: int) -> bool:
        """Static validation utility checking if an age profile is < 365."""
        return age < 365

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  "Height update rejected")
            return False
        self._height = float(height)
        return True

    def set_age(self, days: int) -> bool:
        if days < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  "Age update rejected")
            return False
        self._days = int(days)
        return True

    def show(self) -> None:
        self._stats._show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._days} days old")

    def age(self) -> None:
        self._stats._age_calls += 1
        self._days += 1

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height += self.GROWTH_RATE
        self._height = round(self._height, 1)


class Flower(Plant):
    BASE_H: float = 25.0
    BASE_A: int = 30
    GROWTH_RATE: float = 0.8

    def __init__(
            self, name: str, height: float, days: int, color: str
    ) -> None:
        super().__init__(*(name, height, days))
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
    """Operational subclass designed to track reproductive yields."""
    def __init__(
            self, name: str, height: float, days: int, color: str
    ) -> None:
        super().__init__(*(name, height, days, color))
        self._seed_count: int = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self._seed_count += 42


class Tree(Plant):
    BASE_H: float = 200.0
    BASE_A: int = 365
    GROWTH_RATE: float = 2.5

    class _TreeStats(Plant._Stats):
        """Extended nested class tracking Tree-specific analytics."""
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
            self, name: str, height: float, days: int, trunk_diameter: float
    ) -> None:
        super().__init__(*(name, height, days))
        self.trunk_diameter: float = float(trunk_diameter)
        self._stats = self._TreeStats()  # Overwrite with specialized tracker

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    BASE_H: float = 15.0
    BASE_A: int = 45
    GROWTH_RATE: float = 2.1

    def __init__(
            self, name: str, height: float, days: int, harvest_season: str
    ) -> None:
        super().__init__(*(name, height, days))
        self.harvest_season: str = harvest_season.capitalize()
        self.nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}\n"
              f"Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


def display_statistics(plant: Plant) -> None:
    """Standalone global function demonstrating polymorphic delegation."""
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


def ft_garden_analytics() -> None:
    """Executes the exact curriculum trace for analytics validation."""
    print("=== Tree\n")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()
    display_statistics(oak)

    print("\n=== Seed\n")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("\n[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()

    # Manual setter overrides to perfectly match the PDF's mathematical trace
    # (1 grow / 1 age call, but with a simulated 20-day jump in actual values)
    sunflower.set_height(110.0)
    sunflower.set_age(65)

    sunflower.show()
    print()
    display_statistics(sunflower)

    print("\nAnonymous\n")
    anon = Plant.create_anonymous()
    anon.show()
    display_statistics(anon)


if __name__ == "__main__":
    ft_garden_analytics()
