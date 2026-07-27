import abc


class Creature(abc.ABC):
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

    @abc.abstractmethod
    def attack(self) -> str:
        """
        Abstract method. Every concrete creature MUST implement
        its own unique attack logic.
        """
        pass


class CreatureFactory(abc.ABC):
    """
    Abstract factory pattern blueprint.
    Enforces the creation of both base and evolved creature forms.
    """

    @abc.abstractmethod
    def create_base(self) -> Creature:
        """Spawns the base tier creature of the family."""
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        """Spawns the evolved tier creature of the family."""
        pass