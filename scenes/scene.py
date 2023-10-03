import random

locations = ["Forest", "Mountain", "Beach"]

def random_location():
    if locations:
        current_location = random.choice(locations)
        locations.remove(current_location)
        return current_location
    else:
        return None