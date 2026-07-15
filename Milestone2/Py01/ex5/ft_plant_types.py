#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/15 19:49:22 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/15 19:49:22 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Plant:
    """Base class encapsulating shared attributes and validation."""
    BASE_H: float = 0.0
    BASE_A: int = 0
    GROWTH_RATE: float = 0.5

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name.capitalize()
        self._height: float = 0.0
        self._days: int = 0

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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return False
        else:
            self._height = float(height)
            print(f"Height updated: {int(self._height)}cm")
            return True

    def set_age(self, days: int) -> bool:
        if days < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  "Age update rejected")
            return False
        else:
            self._days = int(days)
            print(f"Age updated: {int(self._days)} days")
            return True

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._days} days old")

    def age(self) -> None:
        self._days += 1

    def grow(self) -> None:
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


class Tree(Plant):
    BASE_H: float = 200.0
    BASE_A: int = 365
    GROWTH_RATE: float = 2.5

    def __init__(
            self, name: str, height: float, days: int, trunk_diameter: float
    ) -> None:
        super().__init__(*(name, height, days))
        self.trunk_diameter: float = float(trunk_diameter)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
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


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    sunflower = Flower("sunflower", 80.0, 45, "yellow")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(0, 20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
