class Pet:
    def __init__(self, name, species):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = 0

        self.health = 100
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def __str__(self):
        return f"{self.name} ({self.species}) | Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}"

    def feed(self):
        self.hunger += 20
        self.happiness += 5
        self.energy -= 5
        self._clamp()

    def play(self):
        self.happiness += 15
        self.energy -= 10
        self.hunger -= 5
        self._clamp()

    def sleep(self):
        self.energy += 20
        self.hunger -= 5
        self._clamp()

    def update_health(self):
        if self.hunger < 30 or self.energy < 30:
            self.health -= 5
        else:
            self.health += 2
        self._clamp()

    def _clamp(self):
        self.health = max(0, min(100, self.health))
        self.hunger = max(0, min(100, self.hunger))
        self.happiness = max(0, min(100, self.happiness))
        self.energy = max(0, min(100, self.energy))
