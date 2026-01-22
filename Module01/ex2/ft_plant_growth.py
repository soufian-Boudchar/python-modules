class Plant:
    """
    A class to represent a plant that can grow and age.
    """
    def __init__(self, name: str, height: int, age_days: int):
        """
        Initialize the plant with name, height, and age.
        """
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self, size: int):
        """
        Increase the plant's height by a specific size.
        """
        self.height += size

    def age(self):
        """
        Increment the plant's age by 1 day.
        """
        self.age_days += 1

    def get_info(self) -> str:
        """
        Return a formatted string with the plant's current status.
        """
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


rose = Plant("Rose", 25, 30)
cactus = Plant("Cactus", 80, 45)
rose_first_hight = rose.height
cactus_first_height = cactus.height
print("=== Day 1 ===")
print(rose.get_info())
print(cactus.get_info())
i = 0
while i < 6:
    rose.grow(1)
    cactus.grow(2)
    rose.age()
    cactus.age()
    i += 1
print("=== Day 7 ===")
print(rose.get_info())
print(f"Growth this week: +{rose.height - rose_first_hight}cm")
print(cactus.get_info())
print(f"Growth this week: +{cactus.height - cactus_first_height}cm")
