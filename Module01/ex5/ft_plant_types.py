class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
#Flower class     
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")  
    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

# Tree class   
class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade\n")
    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
# Vegetable class
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def get_value(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_value}\n")
    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        
def ft_plant_types():
    
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "c")
    
    print("=== Garden Plant Types ===\n")
    
    rose.get_info()
    rose.bloom()
    
    oak.get_info()
    oak.produce_shade()
    
    tomato.get_info()
    tomato.get_value()

ft_plant_types()