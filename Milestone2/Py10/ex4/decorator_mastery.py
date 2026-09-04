import sys
import time
import functools
from collections.abc import Callable
from typing import Any


try:
    from data_generator import FuncMageDataGenerator    # type:  ignore
except ImportError as e:
    print(f"[ERROR] Couldn't import 'data_generator.py'.\n"
          "Please ensure the file is extracted and in the same directory.\n"
          f"{e}")
    sys.exit(1)


def spell_timer(func: Callable) -> Callable:
    """Measures and prints the execution time of a spell."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        
        # Execute the actual spell
        result = func(*args, **kwargs)
        
        end_time = time.time()
        # Format to exactly 3 decimal places as requested
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Validates that the spell has enough power to be cast."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Defensive QA check: Find the power value whether it was passed 
            # as a keyword argument or a positional argument
            power_val = kwargs.get('power')
            if power_val is None:
                # Scan positional arguments from right to left to find the integer
                for arg in reversed(args):
                    if isinstance(arg, int):
                        power_val = arg
                        break
            
            if power_val is None or power_val < min_power:
                return "Insufficient power for this spell"
                
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retries a spell if it fails, up to a maximum number of attempts."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_err_mssg = ""

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_err_mssg = str(e)
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return (f"Spell casting failed after {max_attempts} attempts"
                    f"\n{last_err_mssg}")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Result: Fireball cast!\n"

@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    raise RuntimeError("Waaaaaaagh spelled !")


def main() -> None:
    print("      Master's Tower QA Test Runner      \n",
          ("=" * 42))

    generator = FuncMageDataGenerator
    valid_mages = generator.MAGE_NAMES
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("\nTesting spell timer...")
    print(fireball())

    print("Testing retrying spell...")
    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()

    import random
    test_valid = random.choice(valid_mages)
    test_invalid = random.choice(invalid_names)

    print(f"Is '{test_valid}' valid?"
          f" {MageGuild.validate_mage_name(test_valid)}\n"
          f"Is '{test_invalid}' valid?"
          f" {MageGuild.validate_mage_name(test_invalid)}\n"
          f"{guild.cast_spell('Lightning', 15)}\n"
          f"{guild.cast_spell('Lightning', 5)}")


if __name__ == "__main__":
    main()