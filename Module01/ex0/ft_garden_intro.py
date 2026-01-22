def ft_garden_intro() -> None:
    """
    Displays information about a specific plant in the garden.

    This function initializes variables for a plant's name, height,
    and age, then prints them in a formatted output.
    """
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
