def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit.lower() == "packets"):
        print(f"{quantity} packets available")
    elif (unit.lower() == "grams"):
        print(f"{quantity} grams total")
    elif (unit.lower() == "area"):
        print(f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
