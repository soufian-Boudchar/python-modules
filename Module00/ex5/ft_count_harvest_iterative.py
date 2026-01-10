def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    while (i <= days):
        print("Day", i)
        if (i == days):
            print("Harvest time!")
        i += 1
