from .fire import FlameFactory
from .water import AquaFactory
from .base import Creature, CreatureFactory

# Strict encapsulation: The concrete Creature classes (Flameling, Aquabub, etc.)
# are intentionally omitted from this list to prevent direct instantiation.
__all__ = ["FlameFactory", "AquaFactory", "Creature", "CreatureFactory"]