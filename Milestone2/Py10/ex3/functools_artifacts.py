import sys
import functools
import operator
from collections.abc import Callable
from typing import Any


try:
    from data_generator import FuncMageDataGenerator    #  type: ignore
except ImportError as e:
    print(f"[ERROR] Couldn't import 'data_generator.py'.\n"
          "Please ensure the file is extracted and in the same directory.\n"
          f"{e}")
    sys.exit(1)


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return (0)

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "ice": functools.partial(base_enchantment, 50, "Ice"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative sequence numbers are not supported")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(_arg: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"
    return cast


def dummy_base_spell(power: int, element: str, target: str) -> str:
    return f"Strikes {target} with {power} {element} power"


def main() -> None:
    print("      Ancient Library QA Test Runner     \n",
          ("=" * 42))

    generator = FuncMageDataGenerator
    dynamic_spells = generator.generate_spell_powers(5)

   # 1. Test Spell Reducer
    print("\nTesting spell reduceer...\n"
          f"Base Array: {dynamic_spells}\n"
          f"Sum: {spell_reducer(dynamic_spells, 'add')}\n"
          f"Product: {spell_reducer(dynamic_spells, 'multiply')}\n"
          f"Max: {spell_reducer(dynamic_spells, 'max')}")
    
    # QA trap: Test the error handling
    try:
        spell_reducer(dynamic_spells, "divide")
    except ValueError as e:
        print(f"Error Caught: {e}")

    # 2. Test Partial Enchanter
    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(dummy_base_spell)
    fire_spell = enchanters["fire"]
    # The new fire_spell only requires the 'target' argument now!
    print(f"{fire_spell('Dragon')}\n"
          f"{enchanters['ice']('Goblin')}")

    # 3. Test Memoized Fibonacci
    print("\nTesting memoized fibonacci...\n"
          f"Fib(0): {memoized_fibonacci(0)}\n"
          f"Fib(10): {memoized_fibonacci(10)}\n"
          f"Fib(15): {memoized_fibonacci(15)}\n"
    # Print the cache stats to prove memoization is working
          f"Cache Stats: {memoized_fibonacci.cache_info()}")

    # 4. Test Spell Dispatcher
    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(f"{dispatch(42)}\n"                          # Triggers int
          f"{dispatch('fireball')}\n"                  # Triggers str
          f"{dispatch(['heal', 'shield', 'buff'])}\n"  # Triggers list
          f"{dispatch(3.14)}")                        # Triggers unknown


if __name__ == "__main__":
    main()