# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    light_validator.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 20:46:13 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:48:28 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    if any(ingredient in ingredients.lower() for ingredient in allowed):
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
