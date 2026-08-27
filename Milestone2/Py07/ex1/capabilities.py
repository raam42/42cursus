from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract capability for healing mechanics."""
    
    @abstractmethod
    def heal(self, target: str = "") -> str:
        """Heals the creature or a specified target."""
        pass


class TransformCapability(ABC):
    """Abstract capability for transformation mechanics."""
    
    def __init__(self) -> None:
        """Initializes the persistent state attribute."""
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Triggers the transformation state."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Reverts the transformation state."""
        pass