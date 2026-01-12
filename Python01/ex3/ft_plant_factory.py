#!/usr/bin/env python3

"""
This script shows how to quickly create multiple Plant instances
from a list of data, using a list comprehension.
"""


class Plant:
    """
    Represents a plant with basic characteristics.

    This class stores essential information about a plant including
    its name, current height, and age.

    Attributes:
        name (str): The plant's common name
        height (int): Current height in centimeters
        Age (int): Age of the plant in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant object.

        Creates a plant with starting values for its characteristics.

        Args:
            name (str): The plant's name
            height (int): Height in centimeters
            age (int): Age in days
        """
        self.name = name
        self.height = height
        self.Age = age

    def get_info(self) -> None:
        """
        Display plant information.

        Prints the plant's name, height, and age in a formatted string.
        """
        print(f"Created: {self.name} ({self.height}cm, "
              f"{self.Age} days)")


if __name__ == "__main__":
    # Create a collection of plant data (tuples)
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    # Display header
    print("=== Plant Factory Output ===")
    # Create Plant objects from data and add to list
    for name, height, age in plants_data:
        new_plant = Plant(name, height, age)
        new_plant.get_info()

    # Display total count
    print(f"\nTotal plants created: {len(plants_data)}")
