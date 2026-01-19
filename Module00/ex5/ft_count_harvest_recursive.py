def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def ft_recursive_helper(i):
        if i > days:
            print("Harvest time!")
            return
        print("Day", i)
        ft_recursive_helper(i + 1)
    ft_recursive_helper(1)
