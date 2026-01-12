#!/usr/bin/env python3

"""
Demonstrates inheritance in Python through a plant hierarchy.
Shows how different plant types (Flower, Tree, Vegetable) inherit
common attributes from a base Plant class while adding their own
specialized characteristics and behaviors.
"""


class Plant:
    """
    A base class representing a plant in the garden.

    Attributes:
        name: The common name of the plant
        height: The height of the plant in cm
        Age: The age of the plant in days
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): The plant's name
            height (int): Height in centimeters
            age (int): Age in days
        """
        self.name = name
        self.height = height
        self.Age = age

    def get_info(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.Age} days", end="")


class Flower(Plant):
    """
    A specialized class for Flowers, inheriting from Plant.

    Adds color attribute and blooming behavior specific to flowers.

    Attributes:
        color: The color of the flower petals
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name (str): The flower's name
            height (int): Height in centimeters
            age (int): Age in days
            color (str): The color of the flower
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display a blooming message for the flower."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.Age} days", end="")
        print(f", {self.color} color")


class Tree(Plant):
    """
    A specialized class for Trees, inheriting from Plant.

    Adds trunk diameter attribute and shade calculation functionality.

    Attributes:
        trunk_diameter: The diameter of the tree trunk in cm
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a Tree instance.

        Args:
            name (str): The tree's name
            height (int): Height in centimeters
            age (int): Age in days
            trunk_diameter (int): Trunk diameter in centimeters
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculate and display the shade area provided by the tree.

        Uses formula: trunk_diameter * 1.56 to estimate shade coverage.
        """
        shade_area = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_info(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.Age} days", end="")
        print(f", {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    A specialized class for Vegetables, inheriting from Plant.

    Adds harvest season and nutritional information for vegetables.

    Attributes:
        harvest_season: The optimal season for harvesting
        nutritional_value: Key nutrients or vitamins provided
    """

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name (str): The vegetable's name
            height (int): Height in centimeters
            age (int): Age in days
            harvest_season (str): Best season for harvesting
            nutritional_value (str): Primary nutritional benefit
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
              f"{self.Age} days", end="")
        print(f", {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    # Create and display Flower
    flower1 = Flower("Rose", 25, 30, "red")
    flower1.get_info()
    flower1.bloom()
    print()

    # Create and display Tree
    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.get_info()
    tree1.produce_shade()
    print()
    # Create and display Vegetable
    vegetable1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    vegetable1.get_info()
