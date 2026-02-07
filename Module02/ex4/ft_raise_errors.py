def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    """
    Validates plant health parameters and raises ValueError for invalid inputs. [cite: 91, 529]

    Args:
        plant_name (str): The name of the plant (must not be empty). [cite: 266, 530]
        water_level (int): Water level, must be between 1 and 10. [cite: 267, 531]
        sunlight_hours (int): Sunlight hours, must be between 2 and 12. [cite: 268, 532]
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")

    else:
        return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """
    Demonstrates plant health checks with valid and invalid scenarios. [cite: 91, 536]
    """
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    print(check_plant_health("tomato", 5, 5))

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 6, 100)
    except ValueError as err:
        print(f"Error: {err}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as err:
        print(f"Error: {err}")

    print("\nTesting bad sunlight hours...")

    try:
        check_plant_health("tomato", 7, 0)
    except ValueError as err:
        print(f"Error: {err}")
    print("\nAll error raising tests completed!")


test_plant_checks()
