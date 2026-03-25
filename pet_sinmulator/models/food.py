class Food:
    def __init__(self, name, hunger, happiness, price):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.price = price

foods = [
    Food("Kibble", 20, 5, 0),
    Food("Premium", 30, 15, 5),
    Food("Treat", 10, 25, 3),
]
