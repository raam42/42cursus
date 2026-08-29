#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    tournament.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/29 16:56:40 by rodrigoa         #+#    #+#              #
#    Updated: 2026/08/29 16:56:40 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import itertools
from typing import List, Tuple
from ex0.factory import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)


def battle(
    opponents: List[Tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """
    Executes a round-robin tournament for a given list of opponents.
    Each opponent is a tuple containing their factory and strategy.
    """
    print("*** Tournament ***\n"
          f"{len(opponents)} opponents involved")

    try:
        for p1, p2 in itertools.combinations(opponents, 2):
            print("* Battle *")

            factory_one, strategy_one = p1
            factory_two, strategy_two = p2

            contender_one = factory_one.create_base()
            contender_two = factory_two.create_base()

            print(contender_one.describe(),
                  "vs.",
                  contender_two.describe(),
                  "now fight!")

            print(strategy_one.act(contender_one),
                  strategy_two.act(contender_two))

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)\n"
          "[(Flameling+Normal), (Healing+Defensive)]")
    battle([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error)\n"
          "[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple)\n"
          "[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    battle([
        (aqua, normal),
        (healing, defensive),
        (transform, aggressive)
    ])
