# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    recipes.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 19:38:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 19:41:05 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import elements
from alchemy.potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and"
            f"'{strength_potion()}' mixed with '{elements.create_fire()}'")
