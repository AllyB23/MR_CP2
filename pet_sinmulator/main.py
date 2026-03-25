# MR 1st Pet Simulator
from systems.save_load import save_game, load_game
from models.pet import Pet
from models.food import foods
from systems.shop import buy_food
from systems.competition import compete
from models.breeding import breed

def main():
    print("Welcome to the Pet Simulator!")
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
        print("7. Shop")
        print("8. Compete")
        print("9. Breed")
        print("10. Quit")

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
            print("\n--- SHOP ---")
            for i, food in enumerate(foods):
                print(f"{i+1}. {food.name} (${food.price})")

            pick = int(input("Choose food: ")) - 1
            buy_food(pet, foods[pick])
        elif choice == "8":
            compete(pet)
        elif choice == "9":
            pet2 = Pet("Buddy2", pet.species)
            baby = breed(pet, pet2)
            print(f"New pet born: {baby.name}")
        elif choice == "10":
                break
        else:
            print("Invalid input!")

        pet.update_health()
        pet.age += 1

if __name__ == "__main__":
    main() 
