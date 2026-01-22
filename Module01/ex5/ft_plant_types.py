class SecurePlant:
    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


# Flower class
class Flower(SecurePlant):
    """Specialized plant type: Flower."""

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}"
              f"cm, {self.age} days, {self.color} color")


# Tree class
class Tree(SecurePlant):
    """Specialized plant type: Tree."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}"
              f"cm, {self.age} days, {self.trunk_diameter}cm diameter")


# Vegetable class
class Vegetable(SecurePlant):
    """Specialized plant type: Vegetable."""

    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_value(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}"
              f"cm, {self.age} days, {self.harvest_season} harvest")


rose = Flower("Rose", 25, 30, "red")
tulip = Flower("Tulip", 15, 20, "yellow")

oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 350, 1000, 30)

tomato = Vegetable("Tomato", 80, 90, "summer", "C")
carrot = Vegetable("Carrot", 20, 60, "autumn", "A")

print("=== Garden Plant Types ===\n")

rose.get_info()
rose.bloom()
print()

oak.get_info()
oak.produce_shade()
print()

tomato.get_info()
tomato.get_value()
