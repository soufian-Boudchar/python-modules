class plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():

    # init obj:
    rose = plant("Rose", 25, 30)
    sunflower = plant("Sunflower", 80, 45)
    cactus = plant("Cactus", 15, 120)

    # print infos:
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
    # end func()


ft_garden_data()
