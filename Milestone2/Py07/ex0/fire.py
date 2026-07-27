from .base import Creature, CreatureFactory


class Flameling(Creature):
    """Base tier creature of the Fire family."""
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Evolved tier creature of the Fire family."""
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class FlameFactory(CreatureFactory):
    """Factory dedicated to spawning the Fire family."""
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()