#!/usr/bin/env python3
def water_plants(plant_list):
    """
    Water plants from a list with automatic cleanup.
    Demonstrates try/except/finally structure for resource management.

    Args:
        plant_list: List of plant names to water
    """
    try:
        print("Opening watering system")

        for plant in plant_list:
            if type(plant) is not str or plant == "":
                raise TypeError("invalid plant!")
            print(f"Watering {plant}")

    except TypeError as e:
        print(f"Error: Cannot water {plant} - {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the watering system with both valid and invalid inputs.
    Demonstrates that cleanup always happens via finally block.
    """
    print("=== Garden Watering System ===", end="\n\n")

    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!", end="\n\n")

    print("Testing with error...")
    plant_list = ["tomato", None, "carrots"]
    water_plants(plant_list)
    print()

    print("Cleanup always happens, even with errors!")


test_watering_system()
