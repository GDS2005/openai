from utils.functions import api_openai
import random

class Companion:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        damage = random.randint(5, 10)
        print(f"{self.name} deal {damage} damage to {target}!")
        return damage

    def take_damage(self, damage):
        self.health -= damage


    def talk(self, question):
        print({self.name}>{api_openai(question)})

    def __str__(self):
        return f"{self.name} (Health: {self.health})"