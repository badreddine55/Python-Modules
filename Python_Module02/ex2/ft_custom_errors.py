#!/usr/bin/env python3
class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised when there's a problem with plants."""
    pass


class WaterError(GardenError):
    """Exception raised when there's a problem with watering."""
    pass


def garden_operations():
    """Demonstrate custom exception handling and inheritance."""

    print("Testing PlantError...")
    try:
        watering_days = 25
        if watering_days >= 5:
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}", end="\n\n")

    print("Testing WaterError...")
    try:
        tank_capacity = 10
        if tank_capacity >= 10:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}", end="\n\n")

    print("Testing catching all garden errors...")

    try:
        watering_days = 25
        if watering_days >= 5:
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        watering_days = 25
        if watering_days >= 5:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}", end="\n\n")


def test_error_types():
    """
    Main test function for custom exceptions.
    Shows that custom exception inheritance allows catching
    specific errors or all related errors with a parent class.
    """
    print("=== Custom Garden Errors Demo ===", end="\n\n")
    garden_operations()
    print("All custom error types work correctly!")


test_error_types()
