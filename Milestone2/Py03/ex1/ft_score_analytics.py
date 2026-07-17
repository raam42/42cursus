#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 13:10:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/17 13:10:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def ft_score_analytics() -> None:
    """Processes command-line game scores, sanitizes data, and computes stats."""
    print("=== Player Score Analytics ===")

    valid_scores: list[int] = []

    # Parse and sanitize input data
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    # Halt execution if no valid data was found
    if len(valid_scores) == 0:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2>")
        return

    # Calculate analytics using Python's built-in list functions
    total_players: int = len(valid_scores)
    total_score: int = sum(valid_scores)
    average: float = total_score / total_players
    high_score: int = max(valid_scores)
    low_score: int = min(valid_scores)
    score_range: int = high_score - low_score

    # Display the final crunch
    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average:.1f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()