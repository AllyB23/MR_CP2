# MR 1st Pet Simulator
from systems.save_load import save_game, load_game
from models.pet import Pet

def main():
    name = input("Enter pet name: ")
    species = input("Enter species: ")

    pet = Pet(name, species)

    while True:
        print("\n--- MENU ---")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Status")
        print("5. Save")
        print("6. Load")
        print("7. Quit")

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
            save_game(pet)
        elif choice == "6":
            loaded = load_game()
            if loaded:
                pet = loaded
            elif choice == "7":
                break
        else:
            print("Invalid input!")

        pet.update_health()
        pet.age += 1

if __name__ == "__main__":
    main() 
