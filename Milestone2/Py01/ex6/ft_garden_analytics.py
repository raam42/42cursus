#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/15 23:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/15 23:00:00 by rodrigoa        ###   ########.fr        #
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
        self._height: float = float(height)
        self._days: int = int(days)
        self._stats = self._Stats()

    def show(self) -> None:
        self._stats._show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, {self._days} days old")

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height += self.GROWTH_RATE
        self._height = round(self._height, 1)

    def age(self) -> None:
        self._stats._age_calls += 1
        self._days += 1

    def set_height(self, height: float) -> None:
        self._height = float(height)

    def set_days(self, days: int) -> None:
        self._days = int(days)


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
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
    def __init__(
            self, name: str, height: float, days: int, color: str
    ) -> None:
        super().__init__(name, height, days, color)
        self._seed_count: int = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self._seed_count += 42


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
            self, name: str, height: float, days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter: float = float(trunk_diameter)
        self._stats = self._TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")


def display_statistics(plant: Plant) -> None:
    """Standalone global function for polymorphic analytics."""
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


def main() -> None:
    """Matches the exact execution trace of the curriculum."""
    print("=== Tree\n")
    oak = Tree("oak", 200.0, 365, 5.0)
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
    sunflower.set_height(110.0)
    sunflower.set_days(65)
    sunflower.show()
    print()
    display_statistics(sunflower)

    print("\nAnonymous\n")
    anon = Plant("Unknown plant", 0.0, 0)
    anon.show()
    display_statistics(anon)


if __name__ == "__main__":
    main()
