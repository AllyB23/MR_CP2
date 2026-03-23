# MR 1st Pet Simulator

# Create a pet class
# Create attributes (name, species, age, hunger, happiness, and energy)
# Implement methods or feeding, playing, and putting the pet to sleep

class Animal:
    def __init__(name, species, age, hunger, happiness, energy):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def _str_(self):
        print(f"Name = {self.name} Species")