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


class Plant:
    """Basic plant with name, water_level, and age."""

    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
        """Create a plant with name, water_level (cm),
          and sunlight_hours (days)."""
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Manages a garden with plants and calculates statistics."""

    def __init__(self, plant_name: str) -> None:
        """Create a garden for the owner."""
        self.plant_name = plant_name
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to this garden."""
        self.plants.append(plant)
        print(f"Added {plant.plant_name} successfully")


def check_plant_health(plant_name, water_level, sunlight_hours, p):
    """
    Check if a plant's conditions are healthy.
    Validates plant name, water level, and sunlight hours.

    Args:
        plant_name: Name of the plant (must be non-empty string)
        water_level: Water level (must be between 1-10)
        sunlight_hours: Hours of sunlight (must be between 2-12)
    """
    has_error = False

    try:
        if type(plant_name) is not str or plant_name == "":
            raise PlantError("Plant name cannot be empty!")
    except PlantError as e:
        has_error = True
        print(f"Error adding plant: {e}", end="\n\n")
    try:
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 1)")
    except PlantError as e:
        has_error = True
        print(f"Error checking lettuce: {e}", end="\n\n")
    try:
        if sunlight_hours < 2:
            raise PlantError(f"{sunlight_hours} is too low (min 2)")
        elif sunlight_hours > 12:
            raise PlantError(f"{sunlight_hours} is too high (max 12)")
    except PlantError as e:
        has_error = True
        print(f"Error: Sunlight hours {e}", end="\n\n")

    if not has_error and p == 0:
        return 1
    elif not has_error and p == 1:
        print(f"{plant_name}: healthy (water: {water_level}", end="")
        print(f", sun: {sunlight_hours})")
    else:
        return 0


def watering_tank(list_plant, tank):
    print("Opening watering system")
    try:
        for elment in list_plant:
            if tank > 10:
                print(f"Watering {elment.plant_name} - success")
                tank -= 5
            else:
                raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("Closing watering system (cleanup)", end="\n\n")


def watering_plants(list_plant, tank):
    print("Testing error recovery...")
    try:
        for elment in list_plant:
            if tank > 10:
                print(f"Watering {elment.plant_name} - success")
                tank -= 5
            else:
                raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...", end="\n\n")


def test_plant_checks():
    """
    Test plant health checker with various valid and invalid inputs.
    Demonstrates multiple validation checks using exceptions.
    """
    print("=== Garden Management System ===", end="\n\n")
    print("Adding plants to garden...")
    alice = GardenManager("Alice")
    plant_data = [
        ("tomato", 5, 10),
        ("lettuce", 7, 6),
        ("", 9, 10)
    ]
    for name, water, sunlight in plant_data:
        if check_plant_health(name, water, sunlight, 0):
            plant = Plant(name, water, sunlight)
            alice.add_plant(plant)

    print("Watering plants...")
    watering_tank(alice.plants, 20)
    print("Checking plant health...")
    check_plant_health("tomato", 5, 8, 1)
    check_plant_health("lettuce", 15, 8, 1)
    watering_plants(alice.plants, 1)
    print("All error raising tests completed!")


test_plant_checks()
