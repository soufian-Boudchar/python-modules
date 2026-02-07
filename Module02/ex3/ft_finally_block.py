def water_plants(plant_list: list) -> None:
    """
    Waters a list of plants and ensures the system is closed using a finally block.

    Args:
        plant_list (list): A list of plant names to be watered.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Tests the watering system with both valid and invalid plant lists to
    demonstrate that cleanup always occurs. [cite: 231, 509]
    """
    plants = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plants)
    print("\nTesting with error...")
    plants = ["tomato", None, "lettuce", "carrots"]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
