#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
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
