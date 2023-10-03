import random

class Enemy:
    def __init__(self, location):
        if location == "Forest":
            self.name = "Oso"
            self.health = 30
        if location == "Mountain":
            self.name = "Lobo"
            self.health = 20
        if location == "Beach":
            self.name = "Pirata"
            self.health = 15
        self.experience = 100

    def attack(self, target):
        damage = random.randint(1, 5)
        print(f"{self.name} deal {damage} damage to {target}!")
        return damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def __str__(self):
        return f"{self.name} (Health: {self.health})"