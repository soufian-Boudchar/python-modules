#!/usr/bin/env python3

class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class GardenManager:
    def __init__(self):
        self.plants = []
        
    def add_plant(self, plant_name):
        if not plant_name:
                raise PlantError("Plant name cannot be empty!")
        else:
            self.plants += [plant_name]
            print(f"Added {plant_name} successfully")
            
    def water_plants(self):
        print("Opening watering system")
        
        for plant in self.plants:
            print(f"Watering {plant} - success")
    
        print("Closing watering system (cleanup)")
            
    def check_health(self, name: str, water: int, sun: int):
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
    manager.add_plant("lettuce")
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