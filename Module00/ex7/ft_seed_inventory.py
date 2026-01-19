def ft_seed_inventory(seed_t: str, quantity: int, unit: str) -> None:
    seed = seed_t.capitalize()
    if (unit == "packets"):
        print(seed, "seeds:", quantity, "packets available")
    elif (unit == "grams"):
        print(seed, "seeds:", quantity, "grams total")
    elif (unit == "area"):
        print(seed, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
