# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 15:30:45 by rodrigoa         #+#    #+#              #
#    Updated: 2026/05/20 15:35:23 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {float(self.height)}cm, {self.age} days old")

    def age_one_day(self) -> None:
        self.age += 1

    def grow(self) -> None:
        if self.name == "Rose":
            self.height += 0.8
        elif self.name == "Sunflower":
            self.height += 2.5
        elif self.name == "Cactus":
            self.height += 0.1
        else:
            self.height += 0.5
        self.height = round(self.height, 1)


def ft_plant_growth() -> None:
    if len(sys.argv) != 4:
        print("Usage: python3 ft_plant_growth.py [name] [height] [age]")
        return
    plant_name: str = sys.argv[1]
    try:
        initial_height: float = float(sys.argv[2])
        initial_age: int = int(sys.argv[3])
    except ValueError:
        print("Error: Height MUST be a float and Age MUST be an int.")
        return
    plant = Plant(name=plant_name, height=initial_height, age=initial_age)
    print("=== Garden Plant Growth ===")
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age_one_day()
        plant.show()
    net_growth: float = round(plant.height - initial_height, 1)
    print(f"Growth this week: {net_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
