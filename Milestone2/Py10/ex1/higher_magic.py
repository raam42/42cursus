import random
from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequenced_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequenced_spell


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def is_strong_enough(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    print("      Higher Realm QA Test Runner      \n",
          ("=" * 39))


# Generate dynamic test data mimicking the helper script
    targets = ["Dragon", "Goblin", "Wizard", "Knight"]
    test_target = random.choice(targets)
    test_power = random.randint(5, 25)

    print(f"--- DYNAMIC TEST PARAMETERS ---\n"
          f"Target: {test_target} | Base Power: {test_power}\n")

    # 1. Test Spell Combiner
    print("Testing spell combiner...")
    combo_spell = spell_combiner(fireball, heal)
    combo_result = combo_spell(test_target, test_power)
    print(f"Combined result: {combo_result[0]}, {combo_result[1]}")

    # 2. Test Power Amplifier
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball(test_target, test_power)}\n"
          f"Amplified: {mega_fireball(test_target, test_power)}")

    # 3. Test Conditional Caster
    print("\nTesting conditional caster...")
    picky_spell = conditional_caster(is_strong_enough, heal)
    # Test with both a weak and a strong power level dynamically
    print(f"Weak cast (10): {picky_spell(test_target, 10)}\n"
          f"Dynamic cast ({test_power}): {picky_spell(test_target, test_power)}")

    # 4. Test Spell Sequence
    print("\nTesting spell sequence...")
    combo_attack = spell_sequence([fireball, mega_fireball, heal])
    sequence_results = combo_attack(test_target, test_power)
    for result in sequence_results:
        print(f"- {result}")

if __name__ == "__main__":
    main()