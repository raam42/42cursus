from .factory import CreatureFactory, FlameFactory, AquaFactory

# Strict encapsulation: The concrete Creature classes (Flameling, Aquabub, etc.)
# are intentionally omitted from this list to prevent direct instantiation.
__all__ = ["CreatureFactory", "FlameFactory", "AquaFactory"]