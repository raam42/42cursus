# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 20:49:36 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:52:01 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
