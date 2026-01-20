class Plant:
    def __init__(self, name,height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days
    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age_days} days)"
def ft_plant_factory():
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
ft_plant_factory()