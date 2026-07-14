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
    """
    Model representing a plant with capabilities to grow and age over time,
    demonstrating internal state mutation.
    """

    def __init__(self, name: str, height: float, days: int) -> None:
        """Initializes the plant with starting metrics and a growth rate."""
        self.name: str = name.capitalize()
        self.height: float = float(height)
        self.days: int = days
        self.growth_rate: float = 0.8  # Determines how fast this plant grows

    def show(self) -> None:
        """Displays the encapsulated plant data formatted to one decimal."""
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self) -> None:
        """Increases the plant's height and handles float precision."""
        self.height += self.growth_rate
        self.height = round(self.height, 1)

    def age(self) -> None:
        """Increases the plant's chronological age by one day."""
        self.days += 1


def ft_plant_growth() -> None:
    """
    Simulates a 7-day growth cycle for a Plant object, outputting
    its state changes day-by-day and calculating the total growth.
    """
    rose = Plant("rose", 25.0, 30)
    initial_height: float = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"\n=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    # Calculate total growth over the week
    total_growth: float = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
