#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/14 18:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/14 18:00:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Plant:
    """
    Model representing a plant with encapsulated data to ensure security,
    preventing invalid state mutations through validation.
    """

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes the plant while validating initial metrics."""
        self._name: str = name.capitalize()
        self._growth_rate: float = 0.8
        
        # Validation for height
        if height < 0:
            print(f"{self._name}: Error, height can't be negative. Setting to 0.0")
            self._height = 0.0
        else:
            self._height = float(height)

        # Validation for age
        if age < 0:
            print(f"{self._name}: Error, age can't be negative. Setting to 0")
            self._age = 0
        else:
            self._age = age

    def get_height(self) -> float:
        """Safely returns the protected height attribute."""
        return self._height

    def get_age(self) -> int:
        """Safely returns the protected age attribute."""
        return self._age

    def set_height(self, height: float) -> bool:
        """Validates and updates the plant's height."""
        if height < 0:
            print(f"{self._name}: Error, height can't be negative. Data unchanged.")
            return False
        self._height = float(height)
        return True

    def set_age(self, age: int) -> bool:
        """Validates and updates the plant's age."""
        if age < 0:
            print(f"{self._name}: Error, age can't be negative. Data unchanged.")
            return False
        self._age = age
        return True

    def show(self) -> None:
        """Displays the encapsulated plant data."""
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        """Increases the plant's height and handles float precision."""
        self._height += self._growth_rate
        self._height = round(self._height, 1)

    def age_one_day(self) -> None:
        """Increases the plant's chronological age by one day."""
        self._age += 1


def main() -> None:
    """
    Tests the encapsulation and validation boundaries of the Plant class.
    """
    print("=== Garden Security System ===")
    
    # 1. Testing valid creation
    rose = Plant("rose", 25.0, 30)
    print("Created: ", end="")
    rose.show()
    
    # 2. Testing invalid creation (should fallback to defaults)
    print("\n--- Testing Invalid Instantiation ---")
    cactus = Plant("cactus", -5.0, -10)
    print("Created: ", end="")
    cactus.show()
    
    # 3. Testing invalid updates (should leave data unchanged)
    print("\n--- Testing Invalid Setters ---")
    rose.set_height(-10.0)
    rose.set_age(-5)
    
    # 4. Verifying state protection
    print("\n--- Final State ---")
    rose.show()


if __name__ == "__main__":
    main()
