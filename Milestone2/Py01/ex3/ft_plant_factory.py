#!/bin/python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 15:48:52 by rodrigoa         #+#    #+#              #
#    Updated: 2026/05/20 15:48:52 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name.capitalize()
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.days} days old")

    def age(self) -> None:
        self.days += 1

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


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant(name="rose", height=25.0, days=30),
        Plant(name="oak", height=200.0, days=365),
        Plant(name="cactus", height=5.0, days=90),
        Plant(name="sunflower", height=80.0, days=45),
        Plant(name="fern", height=15.0, days=120),

    ]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
