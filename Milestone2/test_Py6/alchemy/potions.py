# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    potions.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 20:21:40 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:25:07 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import elements
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
    return (f"Healiing potion brewed with '{create_earth()}'"
            f" and '{create_air}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with '{elements.create_fire()}'"
            f"and '{elements.create_water()}'")
