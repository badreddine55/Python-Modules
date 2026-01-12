def ft_count_harvest_recursive(i=1, harvest_recursive=-1):
    if (harvest_recursive == -1):
        harvest_recursive = int(input("Days until harvest:")) + 1
    if (i == harvest_recursive):
        print("Harvest time!")
        return
    else:
        print(f"Day {i}")
        ft_count_harvest_recursive(i + 1, harvest_recursive)
