class Plant:

    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self, size):
        self.height += size

    def age(self):
        self.age_days += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age_days} days old"



rose = Plant("Rose", 25, 30)
first_hight = rose.height
print("=== Day 1 ===")
print(rose.get_info())

for i in range(2, 8):
    rose.grow(1)
    rose.age()
print("=== Day 7 ===")
print(rose.get_info())
print(f"Growth this week: +{rose.height - first_hight}cm")
