# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    dark_validator.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 20:52:31 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:54:29 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    if any(ingredient in ingredients.lower() for ingredient in allowed):
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
