#!/usr/bin/env python3

"""
This script demonstrates object methods and state modification over time.
It shows how objects can have behaviors (methods) that modify their own
internal state, simulating a plant's growth and aging over a week.

This introduces:
- Instance methods that modify object state
- Encapsulation of behavior within the class
- Simulating change over time through method calls
"""


class Plant:
    """
    Represents a plant that can grow and age over time.

    This class extends the basic plant blueprint with methods that
    allow the plant to perform actions on itself, modifying its state.

    Attributes:
        name (str): The plant's common name
        height (int): Starting height in centimeters
        Age (int): Starting age in days
        new_height (int): Additional growth accumulated
        new_age (int): Additional days accumulated
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant object with starting values.

        Args:
            name (str): The plant's name
            height (int): Initial height in centimeters
            age (int): Initial age in days
        """
        self.name = name
        self.height = height
        self.new_height = 0
        self.Age = age
        self.new_age = 0

    def grow(self) -> None:
        """
        Simulate one day of plant growth.

        Increases the plant's height by 1 centimeter.
        """
        self.new_height += 1

    def age(self) -> None:
        """
        Simulate one day passing for the plant.

        Increases the plant's age by 1 day.
        """
        self.new_age += 1

    def get_info(self) -> None:
        """
        Display the plant's current status and growth summary.

        Shows the initial state (Day 1) and current state after growth,
        along with total growth accumulated during the simulation period.
        """
        print("=== Day 1 ===")
        print(f"{self.name}: {self.height}cm, {self.Age} days old")
        print(f"=== Day {self.new_age + 1} ===")
        print(f"{self.name}: {self.height + self.new_height}cm, ", end="")
        print(f"{self.Age + self.new_age} days old")
        print(f"Growth this week: +{self.new_height}cm")


if __name__ == "__main__":
    # Create a plant
    plant1 = Plant("Rose", 25, 30)

    # Simulate 6 days of growth (Day 1 is starting point, so 6 more = Day 7)
    for _ in range(6):
        plant1.grow()
        plant1.age()

    # Display the results
    plant1.get_info()
