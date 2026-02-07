class GardenError(Exception):
    """Base class for exceptions in the garden system."""
    pass


class PlantError(GardenError):
    """Exception raised for errors related to plant conditions."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to water management."""
    pass


class GardenManager:
    """Manages garden operations including
    adding plants and monitoring health."""
    def __init__(self) -> None:
        """Initialize the GardenManager with an empty list of plants."""
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        """Add a plant to the garden after validating the name."""
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        else:
            self.plants += [plant_name]
            print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        """Water all plants in the garden and ensure system cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str, water: int, sun: int) -> None:
        """Check health of a plant based on water and sunlight levels."""
        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        elif water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")
        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        elif sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")
        else:
            print(f"{name}: healthy (water: {water}, sun: {sun})")


print("=== Garden Management System ===\n")

manager = GardenManager()

print("Adding plants to garden...")

try:
    manager.add_plant("tomato")
except GardenError as err:
    print(f"Error adding plant: {err}")
try:
    manager.add_plant("lettuce")
except GardenError as err:
    print(f"Error adding plant: {err}")
try:
    manager.add_plant("")
except GardenError as err:
    print(f"Error adding plant: {err}")
print()
print("Watering plants...")
manager.water_plants()
print()

print("Checking plant health...")
try:
    manager.check_health("tomato", 5, 8)
except GardenError as err:
    print(f"Error checking tomato: {err}")

try:
    manager.check_health("lettuce", 15, 5)
except GardenError as err:
    print(f"Error checking lettuce: {err}")

print()
print("Testing error recovery...")
try:
    raise GardenError("Not enough water in tank")
except GardenError as err:
    print(f"Caught GardenError: {err}")

print("System recovered and continuing...\n")
print("Garden management system test complete!")
