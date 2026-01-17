# USE tuples TO store 3D coordinates (x,y, z)
# USE try/except blocks to handle parsing errors when convertingstring input
# to numbers.
import sys
import math


def Parsing_coordinates(x, y, z) -> bool:
    try:
        int(x), int(y), int(z)
        return True
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{x},{y},{z}"')
        print(f"Error parsing coordinates: {e}")
        print('Error details - Type: ValueError, Args: ("{}" )'.format(e))
        return False


def Distance(x1, y1, z1, x2, y2, z2, pars):
    res = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    if pars == 1:
        print(f"Position created: {x2, y2, z2}")
    print(f"Distance between {x1, y1, z1} and ", end="")
    print(f"{x2, y2, z2} : {res:.2f}")


def Unpacking(x, y, z):
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    if len(sys.argv) >= 1:
        print("=== Game Coordinate System ===")
        my_list = [10, 20, 5]
        if Parsing_coordinates(*my_list) is True:
            coordinates = tuple(my_list)
            print("Position created: ", end="")
            print(f"{coordinates[0], coordinates[1], coordinates[2]}")
            Distance(0, 0, 0, *coordinates, 0)
            print()
        my_list = [3, 4, 0]
        if Parsing_coordinates(*my_list) is True:
            coordinates = tuple(my_list)
            Distance(0, 0, 0, *coordinates, 1)
            print()
        my_list = ["abc", "def", "ghi"]
        if Parsing_coordinates(*my_list) is True:
            coordinates = tuple(my_list)
            Distance(0, 0, 0, *coordinates, 1)
        print()
        my_list = [3, 4, 0]
        if Parsing_coordinates(*my_list) is True:
            coordinates = tuple(my_list)
            Unpacking(*coordinates)
