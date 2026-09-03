import random
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power_added: int) -> int:
        nonlocal total_power
        total_power += power_added
        return total_power
    return accumulator


def enchanment_factory(enchanment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchanment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}


    def store(key: str, value: Any) -> None:
        vault[key] = value


    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:
    print("       Memory Depths QA Test Runner      \n",
          ("=" * 42))

    # Mimicking the data generator's Exercise 2 payload[cite: 3]
    initial_powers = [random.randint(20, 80) for _ in range(3)]
    power_additions = [random.randint(5, 20) for _ in range(5)]
    enchanment_types = ["Flaming", "Frozen", "Shocking", "Earthen"]
    items_to_enchant = ["Sword", "Shield", "Staff", "Amulet"]

    # 1. Test Mage Counter
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}\n"
          f"counter_a call 2: {counter_a()}\n"
    # Proves counter_b has its own completely isolated memory state
          f"counter_b call 1: {counter_b()}")

    # 2. Test Spell Accumulator
    print("\nTesting spell accumulator...")
    base_power = initial_powers[0]
    add_1 = power_additions[0]
    add_2 = power_additions[1]
    
    accumulator = spell_accumulator(base_power)
    print(f"Base {base_power}, add {add_1}: {accumulator(add_1)}\n"
          f"Current total, add {add_2}: {accumulator(add_2)}")

    # 3. Test Enchantment Factory
    print("\nTesting enchantment factory...")
    selected_enchants = random.sample(enchanment_types, 2)
    
    factory_1 = enchanment_factory(selected_enchants[0])
    factory_2 = enchanment_factory(selected_enchants[1])
    
    print(factory_1(items_to_enchant[0]))
    print(factory_2(items_to_enchant[1]))

    # 4. Test Memory Vault
    print("\nTesting memory vault...")
    vault = memory_vault()
    store_func = vault['store']
    recall_func = vault['recall']
    
    test_val = random.randint(10, 99)
    print(f"Store 'secret' = {test_val}")
    store_func('secret', test_val)
    
    print(f"Recall 'secret': {recall_func('secret')}\n"
          f"Recall 'unknown': {recall_func('unknown')}")


if __name__ == "__main__":
    main()