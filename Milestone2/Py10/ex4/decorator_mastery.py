import time
import functools
from collections.abc import Callable
from typing import Any


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
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


