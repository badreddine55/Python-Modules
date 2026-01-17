#!/usr/bin/env python3
def check_temperature(temp_str):
    """
    Check if temperature is safe for plants.

    Args:
        temp_str: Temperature as a string
    """
    try:
        # Convert string to integer
        number = int(temp_str)
        print(f"Testing temperature: {number}")

        # Check if temperature is too hot
        if number >= 40:
            print(f"Error: {number}°C is too hot for plants (max 40°C)")
        # Check if temperature is too cold
        elif number <= 0:
            print(f"Error: {number}°C is too cold for plants (min 0°C)")
        # Temperature is in valid range
        else:
            print(f"Temperature {number}°C is perfect for plants!")

    except ValueError:
        # Handle invalid input that can't be converted to number
        print(f"Testing temperature: {temp_str}")
        print(f"Error: '{temp_str}' is not a valid number")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()

    # Test valid temperature
    check_temperature("25")
    print()

    # Test invalid input (not a number)
    check_temperature("abc")
    print()

    # Test temperature too hot
    check_temperature("100")
    print()

    # Test temperature too cold
    check_temperature("-50")
    print()

    print("All tests completed - program didn't crash!")
