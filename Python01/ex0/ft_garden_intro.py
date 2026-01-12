#!/usr/bin/env python3

"""
This is the first program in the  Garden Systems series.
It demonstrates the basic structure of a Python program including
simple variable usage to display plant information.

This script shows:
- How to use the if __name__ == "__main__" pattern
- Basic variable assignment
- Simple output formatting with print()
"""

if __name__ == "__main__":
    # Plant information variables
    name = "Rose"
    height = 25
    age = 30

    # Display garden welcome message
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")
