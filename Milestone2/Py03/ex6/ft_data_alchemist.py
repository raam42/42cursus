#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_alchemist.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/19 19:54:35 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/19 19:54:35 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import random


def ft_data_alchemist() -> None:
    """Demonstrates list and dictionary comprehensions."""
    print("=== Game Data Alchemist ===\n")

    initial_players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    all_capitalized: list[str] = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized: list[str] = [name for name in initial_players if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized}")

    score_dict: dict[str, int] = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"\nScore dict: {score_dict}")

    average_score: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average_score, 2)}")

    high_scores: dict[str, int] = {name: score for name, score in score_dict.items() if score > average_score}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()