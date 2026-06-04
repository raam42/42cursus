#!/bin/python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/06/04 17:10:49 by rodrigoa         #+#    #+#              #
#    Updated: 2026/06/04 17:10:49 by rodrigoa        ###   ########.fr        #
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
    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unkown plant", height=cls.BASE_H, age=cls.BASE_A)
    @staticmethod
    def ver_age(age: int) -> bool:
        return age < 365:
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


def ft_garden_analytics() -> None:
    validated_age = Plant.ver_age(Plant._age)
    print(f"=== Garden statistics ===\n
          === Check year-old\n
          Is {Plant._age} more than a year? -> {validated_age}")


if __name__ == "__main__":
