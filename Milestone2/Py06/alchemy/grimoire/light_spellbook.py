# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    light_spellbook.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 20:42:31 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:55:31 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
