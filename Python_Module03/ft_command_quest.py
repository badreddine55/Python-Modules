import sys

if __name__ == "__main__":
    number = len(sys.argv)
    print("=== Command Quest ===")
    if number == 1:
        print("No arguments provided!")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received:{number - 1}")
        for i in range(1, number):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {number}")
