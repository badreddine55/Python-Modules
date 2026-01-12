#!/usr/bin/env python3

"""
This script demonstrates the use of a class as a blueprint for creating
multiple objects with similar attributes. It shows how to organize plant
data efficiently using a Plant class instead of managing individual
variables for each plant.

This introduces:
- Class definition and instantiation
- The __init__ constructor method
- Instance attributes (self.attribute)
- Creating multiple objects from the same class
"""


class Plant:
    """
    Blueprint for representing a plant with basic attributes.

    This class serves as a template for creating plant objects,
    each with their own name, height, and age.

    Attributes:
        name (str): The plant's common name
        height (int): Current height in centimeters
        age (int): Age in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant object.

        Args:
            name (str): The plant's name
            height (int): Height in centimeters
            age (int): Age in days
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    # Create three different plant objects
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    # Display the garden plant registry
    print("=== Garden Plant Registry ===")
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
