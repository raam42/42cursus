from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    """Abstract strategy defining tournament battle behavior."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """
        Checks if the creature possesses 
        the necessary capabilities for this strategy.
        """
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """Executes the strategy's combat sequence."""
        pass


class NormalStrategy(BattleStrategy):
    """A basic strategy that simply attacks. Valid for any creature."""
    
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """A stateful strategy that transforms, attacks, and reverts."""
    
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy")

        assert isinstance(creature, TransformCapability)

        actions = [
            creature.transform(),
            creature.attack(),
            creature.revert()
        ]
        return "\n".join(actions)


class DefensiveStrategy(BattleStrategy):
    """A conservative strategy that attacks, then heals."""
    
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy")
            
        assert isinstance(creature, HealCapability)

        actions = [
            creature.attack(),
            creature.heal()
        ]
        return "\n".join(actions)