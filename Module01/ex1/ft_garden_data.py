class Plant:
    """
    A class to represent a plant in the garden.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in cm.
        age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a new plant with its starting values.
        """
        self.name = name
        self.height = height
        self.age = age


# init obj:
rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

# print infos:
print("=== Garden Plant Registry ===")
print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
# end func()
