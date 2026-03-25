def buy_food(pet, food):
    if pet.money >= food.price:
        pet.money -= food.price
        pet.inventory.append(food)
        print(f"Bought {food.name}")
    else:
        print("Not enough money!")
