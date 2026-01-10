def ft_recursive_helper(days, i):
    if (i > days):
        print("Harvest time!")
        return
    print("Day", i)
    ft_recursive_helper(days, i + 1)


def ft_count_harvest_recursive():
    i = 1
    days = int(input("Days until harvest: "))
    ft_recursive_helper(days, i)
