class Plant:
    """
    A class to represent a plant with initial characteristics.
    """
    def __init__(self, name: str, height: int, age_days: int):
        """
        Initialize a new plant with its starting values.
        """
        self.name = name
        self.height = height
        self.age_days = age_days

    def get_info(self) -> str:
        """
        Return the plant's details as a formatted string.
        """
        return f"{self.name} ({self.height}cm, {self.age_days} days)"


seeds_data = [("Rose", 25, 30),
              ("Oak", 200, 365),
              ("Cactus", 5, 90),
              ("Sunflower", 80, 45),
              ("Fern", 15, 120)]
count = 0
print("=== Plant Factory Output ===")
for seed in seeds_data:
    new_plant = Plant(seed[0], seed[1], seed[2])
    print(f"Created: {new_plant.get_info()}")
    count += 1
print(f"\nTotal plants created: {count}")
