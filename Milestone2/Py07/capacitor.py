#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    capacitor.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/29 16:38:56 by rodrigoa         #+#    #+#              #
#    Updated: 2026/08/29 16:38:56 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability
)


def test_healing_creatures() -> None:
    """Tests the full lifecycle of a healing capability creature."""
    try:
        print("Testing Creature with healing capability\nbase: ")
        factory = HealingCreatureFactory()

        base = factory.create_base()
        print(base.describe(),
              base.attack())

        if isinstance(base, HealCapability):
            print(base.heal())

        print("evolved:")
        evolved = factory.create_evolved()
        print(evolved.describe(),
              evolved.attack())

        if isinstance(evolved, HealCapability):
            print(evolved.heal())

    except Exception as e:
        print(f"Healing test failed: {e}")


def test_transforming_creatures() -> None:
    """Tests the stateful mechanics of a transforming capability creature."""
    try:
        print("Testing Creature with transform capability\nbase:")
        factory = TransformCreatureFactory()

        base = factory.create_base()
        print(base.describe(),
              base.attack())

        if isinstance(base, TransformCapability):
            print(base.transform(),
                  base.attack(),
                  base.revert())

        print("evolved:")
        evolved = factory.create_evolved()
        print(evolved.describe(),
              evolved.attack())

        if isinstance(evolved, TransformCapability):
            print(evolved.transform(),
                  evolved.attack(),
                  evolved.revert())

    except Exception as e:
        print(f"Transform test failed: {e}")


if __name__ == "__main__":
    test_healing_creatures()
    test_transforming_creatures()
