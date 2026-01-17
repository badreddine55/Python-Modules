#!/usr/bin/env python3
def garden_operations():
    """Demonstrate different types of built-in Python exceptions."""
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError:  {e}", end="\n\n")

    print("Testing ZeroDivisionError...")
    try:
        print(f"{5/0}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}", end="\n\n")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e.args[1]}")
        print()

    print("Testing KeyError...")
    try:
        plant = {"name": "Rose", "height": 21}
        print(plant["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}", end="\n\n")

    print("Testing multiple errors together...")
    try:
        int("badr")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!", end="\n\n")


def test_error_types():
    """
    Main test function to demonstrate exception handling.
    Shows that programs can handle errors gracefully without crashing.
    """
    print("=== Garden Error Types Demo ===", end="\n\n")
    garden_operations()
    print("All error types tested successfully!")


test_error_types()
