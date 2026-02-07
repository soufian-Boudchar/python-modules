class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems (e.g., wilting)."""
    pass


class WaterError(GardenError):
    """Exception raised for watering issues (e.g., empty tank)."""
    pass


def err_test():
    """
    Tests and demonstrates custom exception raising and catching, 
    including inheritance behavior. [cite: 91, 483]
    """
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


err_test()
