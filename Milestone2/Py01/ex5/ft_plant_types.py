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


class Plant:
    BASE_H: float = 0.0
    BASE_A: int = 0
    GROWTH_RATE: float = 0.5

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self._height: float = 0.0
        self._age: int = 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print(
                f"Creation fallback: default height set to {self.BASE_H}cm")
            self._height = float(self.BASE_H)
        else:
            self._height = float(height)
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print(
                f"Creation fallback: default age set to {self.BASE_A} days")
            self._age = int(self.BASE_A)
        else:
            self._age = int(age)
#        print(f"Plant created: {self.name}: {self._height}cm, "
#              f"{self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return False
        else:
            self._height = float(height)
            print(f"Height updated: {int(self._height)}cm")
            return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  f"Age update rejected")
            return False
        else:
            self._age = int(age)
            print(f"Age updated: {int(self._age)} days")
            return True

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height += self.GROWTH_RATE
        self._height += round(self._height, 1)
        if hasattr(self, "nutritional_value"):
            self.nutritional_value += 1


class Flower(Plant):
    BASE_H: float = 25.0
    BASE_A: int = 30
    GROWTH_RATE: float = 0.8

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(*(name, height, age))
        self.color: str = color
        self._is_blooming: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self._is_blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully")

    def bloom(self) -> None:
        self.show()
        print(f"[asking the {self.name} to bloom]")
        self._is_blooming = True


class Tree(Plant):
    BASE_H: float = 200.0
    BASE_A: int = 365
    GROWTH_RATE: float = 2.5

    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(*(name, height, age))
        self.trunk_diameter: float = float(trunk_diameter)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"{self.name} Tree now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    BASE_H: float = 15.0
    BASE_A: int = 45
    GROWTH_RATE: float = 2.1

    def __init__(self,
                 name: str, height: float, age: int, harvest_season: str,
                 days_to_harvest: int) -> None:
        super().__init__(*(name, height, age))
        self.harvest_season: str = harvest_season.capitalize()
        self.nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}\n"
              f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    if len(sys.argv) < 6:
        print("Correct usage parameters below...\n"
              "Flower: python3 ft_plant_types.py flower "
              "[flower name][h][a][color]\n"
              "Tree: python3 ft_plant_types.py tree "
              "[tree name][h][a][diameter]\n"
              "Veggie: python3 ft_plant_types.py vegetable "
              "[vegetable name][h][a][season month][days]")
        return

    species_type: str = sys.argv[1].capitalize()
    try:
        initial_height: float = float(sys.argv[3])
        initial_age: int = int(sys.argv[4])
    except Exception:
        print("Error: Height MUST be a float & Age MUST be an int")
        return

    print("=== Garden Plant Types ===")
    print("===", species_type)
    if species_type == "Flower":
        if len(sys.argv) != 6:
            print("Error: required parameters "
                  "Flower [flower name] [height][age][color]")
            return

        flower = Flower(sys.argv[2], initial_height, initial_age, sys.argv[5])
        flower.show()
        flower.bloom()
        flower.show()

    elif species_type == "Tree":
        if len(sys.argv) != 6:
            print("Error: required parameters "
                  "Tree [tree name] [height][age][diameter]")
            return
        try:
            diameter = float(sys.argv[5])
            if diameter < 0:
                print("Error: diameter can't be negative")
                return
        except Exception:
            print("Error: Trunk diameter must be a float")
            return
        tree = Tree(sys.argv[2], initial_height, initial_age, diameter)
        tree.show()
        tree.produce_shade()

    elif species_type == "Vegetable":
        if len(sys.argv) != 7:
            print("Error: required parameters "
                  "Vegetable [veggie name] [height][age][month][days]"
                  )
            return
        veggie = Vegetable(sys.argv[2], initial_height,
                           initial_age, sys.argv[5], int(sys.argv[6]))
        veggie.show()
        print(f"[make {veggie.name.lower()} "
              f"grow and age for {sys.argv[6]} days]")
        for i in range(int(sys.argv[6])):
            veggie.grow()
            veggie.age()
        veggie.show()


if __name__ == "__main__":
    ft_plant_types()
