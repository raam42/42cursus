import elements
import alchemy.elements


def healing_potion() -> str:
    """Brew a healing potion using Earth and Air."""
    return (f"Healing potion brewed with"
            f"{elements.create_earth()} and {elements.create_air()}.")


def strength_potion() -> str:
    """Brew a strength potion using Fire and Water."""
    return (f"Strength potion brewed with"
            f"{elements.create_fire} and {elements.create_water}.")