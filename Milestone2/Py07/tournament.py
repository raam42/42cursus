#!/usr/bin/env python3
import itertools
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)


def run_tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """
    Executes a round-robin tournament for a given list of opponents.
    Each opponent is a tuple containing their factory and strategy.
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        # itertools.combinations perfectly generates unique 1-on-1 matchups
        for p1, p2 in itertools.combinations(opponents, 2):
            print("* Battle *")

            # Extract factories and strategies from the tuples
            factory_one, strategy_one = p1
            factory_two, strategy_two = p2

            # Spawn the base tier contenders
            contender_one = factory_one.create_base()
            contender_two = factory_two.create_base()

            print(contender_one.describe())
            print("VS.")
            print(contender_two.describe())
            print("now fight!")

            # Execute the combat sequence
            strategy_one.act(contender_one)
            strategy_two.act(contender_two)

    except InvalidStrategyError as e:
        # FQA Safeguard: Catches invalid pairings and gracefully aborts
        print(f"Battle error, aborting tournament: {e}")
    except Exception as e:
        # Catch-all for any unexpected runtime crashes
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # 1. Spin up the factories (The Asset Pipelines)
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    # 2. Instantiate the strategies (The AI Behaviors)
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # 3. Execute the test scenarios
    print("Tournament 0 (basic)\n"
          "[(Flameling+Normal), (Healing+Defensive)]")
    run_tournament([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error)\n"
          "[(Flameling+Aggressive), (Healing+Defensive)]")
    run_tournament([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple)\n"
          "[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    run_tournament([
        (aqua, normal), 
        (healing, defensive), 
        (transform, aggressive)
    ])