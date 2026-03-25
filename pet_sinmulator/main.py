# MR 1st Pet Simulator

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

def _clamp(self):
    self.hunger = max(0, min(100, self.hunger))
    self.happiness = max(0, min(100, self.happiness))
    self.energy = max(0, min(100, self.energy))
    self.health = max(0, min(100, self.health))

def update_health(self):
    if self.hunger < 30 or self.energy < 30:
        self.health -= 5
    else:
        self.health += 2
    self._clamp()

def main():
    name = input("Enter pet name: ")
    species = input("Enter species: ")

    pet = Pet(name, species)

    time = 0

    while True:
        print("\n--- MENU ---")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Status")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            print(pet)
        elif choice == "5":
            break
        else:
            print("Invalid input!")

        time += 1
        pet.age += 1
        pet.update_health()

if __name__ == "__main__":
    main()

