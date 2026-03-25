import json
from models.pet import Pet

def save_game(pet):
    with open("data/saves.json", "w") as f:
        json.dump(pet.__dict__, f)

def load_game():
    try:
        with open("data/saves.json", "r") as f:
            data = json.load(f)
            pet = Pet(data["name"], data["species"])
            pet.__dict__.update(data)
            return pet
    except:
        print("No save file found.")
        return None
