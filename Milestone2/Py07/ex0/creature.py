from abc import ABC, abstractmethod


class Creature(ABC):
    """
    Abstract base class defining the mandatory structure
    for all creature entities in the game.
    """

    def __init__(self, name: str, creature_type: str) -> None:
        """Initialize the creature with a name and an elemental type."""
        self.name: str = name
        self.type: str = creature_type

    def describe(self) -> str:
        """
        Concrete generic method that returns a standard description.
        """
        return f"{self.name} is a {self.type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        """
        Abstract method. Every concrete creature MUST implement
        its own unique attack logic.
        """
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
