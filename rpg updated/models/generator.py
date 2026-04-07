import random
from faker import Faker
from models.character import Character

class RandomGenerator:
    def __init__(self):
        self.fake = Faker()
        self.races = ("Human", "Elf", "Orc")
        self.classes = ("Fighter", "Wizard", "Rogue")

    def generate_random_character(self):
        name = self.fake.name()
        race = random.choice(self.races)
        char_class = random.choice(self.classes)
        level = random.randint(1, 15)
        # Generate random stats between 3 and 18
        attributes = [random.randint(3, 18) for _ in range(4)]
        return Character(name, race, char_class, level, attributes)
