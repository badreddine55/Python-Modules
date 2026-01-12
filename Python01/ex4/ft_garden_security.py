#!/usr/bin/env python3

"""

A Secure Plant class that uses encapsulation to protect its data.
Direct access to height and age is discouraged;
setters are used for validation.

"""


class SecurePlant:
    """
    Represents a plant with protected characteristics and validation.

    This class uses private attributes (name mangling with __) to prevent
    direct access to height and age. All modifications go through setter
    methods that validate the data before updating.

    Attributes:
        name: The plant's common name (string, public)
        __height: Current height in centimeters (int, private)
        __Age: Age of the plant in days (int, private)
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new SecurePlant object.

        Creates a plant with a name and sets initial height and age to 0.

        Args:
            name (str): The plant's name
        """
        self.name = name
        self.__height = None
        self.__Age = None
        print(f"Plant created: {self.name}")
        self.set_age(age)
        self.set_height(height)

    def get_height(self) -> int:
        """
        Retrieve the current height of the plant.

        Returns:
            int: Height in centimeters
        """
        return self.__height

    def get_age(self) -> int:
        """
        Retrieve the current age of the plant.

        Returns:
            int: Age in days
        """
        return self.__Age

    def set_height(self, new_height) -> bool:
        """
        Update the plant's height with validation.

        Validates that the new height is non-negative before updating.
        Rejects negative values with an error message.

        Args:
            new_height (int): New height in centimeters

        """
        if new_height < 0:
            print("Invalid operation attempted: height", end="")
            print(f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return False
        else:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")
            return True

    def set_age(self, new_age) -> bool:
        """
        Update the plant's age with validation.

        Validates that the new age is non-negative before updating.
        Rejects negative values with an error message.

        Args:
            new_age (int): New age in days

        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} day [REJECTED]")
            print("Security: Negative age rejected")
            return False
        else:
            self.__Age = new_age
            print(f"Age updated: {new_age} days [OK]")
            return True


if __name__ == "__main__":
    print("=== Garden Security System ===")
    # Create a secure plant object
    plant1 = SecurePlant("Rose", 25, 30)

    print()
    # Invalid operation (security test)
    plant1.set_height(-5)
    print()

    # Display final state
    print(f"Current plant: {plant1.name} ({plant1.get_height()}cm", end="")
    print(f", {plant1.get_age()} days)")
