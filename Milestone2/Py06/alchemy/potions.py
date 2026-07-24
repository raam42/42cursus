import elements
import Py06.elements


def healing_potion() -> str:
    return (f"Healing potion brewed with"
            f"{elements.create_earth()} and {elements.create_air()}.")


def strength_potion() -> str:
    return (f"Strength potion brewed with"
            f"{Py06.elements.create_fire} and {Py06.elements.create_water}.")