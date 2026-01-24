#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
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
    plants = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plants)
    print("\nTesting with error...")
    plants = ["tomato", None, "lettuce", "carrots"]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")
    
test_watering_system()