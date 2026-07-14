#!/bin/python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 13:56:22 by rodrigoa         #+#    #+#              #
#    Updated: 2026/05/20 13:56:22 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {int(self.height)}cm, {self.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant(name="Rose", height=25, age=30)
    sunflower = Plant(name="Sunflower", height=80, age=45)
    cactus = Plant(name="Cactus", height=15, age=120)
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
