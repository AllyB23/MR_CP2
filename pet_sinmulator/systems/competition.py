import random

def compete(pet):
    score = random.randint(0, 100)
    print(f"{pet.name} scored {score}!")

    if score > 60:
        pet.level += 1
        pet.money += 10
        print(" You won! +Level +$10")
    else:
        print(" You lost!")
