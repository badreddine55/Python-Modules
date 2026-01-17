alicea = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
           'speed_demon', 'perfectionist'}


def print_set(data):
    nbr = len(data)
    for achievement in data:
        print(f"'{achievement}'", end="")
        nbr -= 1
        if nbr > 0:
            print(" ,", end="")
    print("}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    print("Player alice achievements: {", end="")
    print_set(alicea)
    print("Player bob achievements: {", end="")
    print_set(bob)
    print("Player charlie achievements: {", end="")
    print_set(charlie)
    print("\n=== Achievement Analytics ===")
    print("All unique achievements:")
    unique = alicea.union(bob, charlie)
    print_set(unique)
    print(f"Total unique achievements: {len(unique)}\n")
    common_all = alicea.intersection(bob, charlie)
    print("Common to all players: {", end="")
    print_set(common_all)
    Rare = alicea.difference(bob, charlie)
    Rare = Rare.union(bob.difference(alicea, charlie))
    Rare = Rare.union(charlie.difference(alicea, bob))
    print("Rare achievements (1 player): {", end="")
    print_set(Rare)
    common_a_b = alicea.intersection(bob)
    print("\nAlice vs Bob common: {", end="")
    print_set(common_a_b)
    unique_a = alicea.difference(bob)
    print("Alice unique: {", end="")
    print_set(unique_a)
    unique_b = bob.difference(alicea)
    print("Bob unique: {", end="")
    print_set(unique_b)
