from faker import Faker

fake = Faker()

class Character:
    def __init__(self, name, race, char_class, level=1, attributes=None):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level
        # Attributes: [Strength, Intelligence, Wisdom, Charisma]
        self.attributes = attributes if attributes else [5, 5, 5, 5]
        self.skills = set()
        self.inventory = {"starter weapon"}
        self.backstory = fake.paragraph(nb_sentences=3)

    def to_dict(self):
        """Returns character data as a dictionary for Pandas conversion."""
        return {
            "Name": self.name,
            "Race": self.race,
            "Class": self.char_class,
            "Level": self.level,
            "Strength": self.attributes[0],
            "Intelligence": self.attributes[1],
            "Wisdom": self.attributes[2],
            "Charisma": self.attributes[3]
        }
