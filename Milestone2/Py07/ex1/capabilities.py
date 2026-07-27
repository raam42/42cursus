import abc


class HealCapability(abc.ABC):
    """Abstract capability for healing mechanics."""
    
    @abc.abstractmethod
    def heal(self, target: str = "") -> str:
        """Heals the creature or a specified target."""
        pass


class TransformCapability(abc.ABC):
    """Abstract capability for transformation mechanics."""
    
    def __init__(self) -> None:
        """Initializes the persistent state attribute."""
        self.is_transformed: bool = False

    @abc.abstractmethod
    def transform(self) -> str:
        """Triggers the transformation state."""
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        """Reverts the transformation state."""
        pass