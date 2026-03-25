from models.pet import Pet

def breed(pet1, pet2):
    name = pet1.name + pet2.name
    baby = Pet(name, pet1.species)

    baby.happiness = (pet1.happiness + pet2.happiness) // 2

    return baby
