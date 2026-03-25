import random

def random_event(pet):
    events = [
        ("found a toy", 10),
        ("got sick", -10),
        ("made a friend", 15),
    ]

    event = random.choice(events)
    pet.happiness += event[1]

    print(f"\n EVENT: {pet.name} {event[0]}! ({event[1]} happiness)")
