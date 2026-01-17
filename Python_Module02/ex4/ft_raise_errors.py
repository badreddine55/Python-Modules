#!/usr/bin/env python3
def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Check if a plant's conditions are healthy.
    Validates plant name, water level, and sunlight hours.

    Args:
        plant_name: Name of the plant (must be non-empty string)
        water_level: Water level (must be between 1-10)
        sunlight_hours: Hours of sunlight (must be between 2-12)
    """
    flag = 0

    try:
        if type(plant_name) is not str or plant_name == "":
            raise ValueError("Plant name cannot be empty!")
    except ValueError as e:
        flag += 1
        print(f"Error: {e}", end="\n\n")

    try:
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
    except ValueError as e:
        flag += 1
        print(f"Error: {e}", end="\n\n")

    try:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low  (min 1)")
    except ValueError as e:
        flag += 1
        print(f"Error: {e}", end="\n\n")

    try:
        if sunlight_hours < 2:
            raise ValueError(f"{sunlight_hours}  is too low (min 2)")
    except ValueError as e:
        flag += 1
        print(f"Error: Sunlight hours {e}", end="\n\n")

    try:
        if sunlight_hours > 12:
            raise ValueError(f"{sunlight_hours} is too high (max 12)")
    except ValueError as e:
        flag += 1
        print(f"Error: Sunlight hours {e}", end="\n\n")

    if flag == 0:
        print(f"Plant '{plant_name}' is healthy!", end="\n\n")


def test_plant_checks():
    """
    Test plant health checker with various valid and invalid inputs.
    Demonstrates multiple validation checks using exceptions.
    """
    print("=== Garden Plant Health Checker ===", end="\n\n")

    print("Testing good values...")
    check_plant_health("tomato", 5, 6)

    print("Testing empty plant name...")
    check_plant_health("", 7, 3)

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 6)

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 7, 0)

    print("All error raising tests completed!")


test_plant_checks()
