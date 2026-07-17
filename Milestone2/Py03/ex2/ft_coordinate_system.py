#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 13:30:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/17 13:30:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompts the user for 3D coordinates, handles errors, and returns a tuple."""
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(',')
        
        # Check if we have exactly 3 parts
        if len(parts) != 3:
            print("Invalid syntax")
            continue
            
        coords: list[float] = []
        error_found = False
        
        # Validate each part individually to provide precise error messages
        for part in parts:
            part = part.strip()
            try:
                coords.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                error_found = True
                break  # Stop processing the rest of the tuple on first error
                
        # If all 3 parts were parsed successfully, lock them into a tuple
        if not error_found:
            return (coords[0], coords[1], coords[2])


def calculate_distance(
        p1: tuple[float, float, float], p2: tuple[float, float, float]
) -> float:
    """Calculates the Euclidean distance between two 3D points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)


def ft_coordinate_system() -> None:
    """Executes the coordinate tracking and distance calculations."""
    print("Game Coordinate System")
    
    # 1. First set of coordinates
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    
    # Calculate distance from origin (0, 0, 0)
    origin: tuple[float, float, float] = (0.0, 0.0, 0.0)
    dist_to_center = calculate_distance(origin, pos1)
    print(f"Distance to center: {round(dist_to_center, 4)}")
    
    # 2. Second set of coordinates
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    
    # Calculate distance between the two points
    dist_between = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    ft_coordinate_system()