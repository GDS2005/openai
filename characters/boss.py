import random

class Boss:
    def __init__(self, location):
        if location == "Forest":
            self.name = "Thira el Arbol Antiguo"
            self.health = 100
        if location == "Mountain":
            self.name = "Gigante de Hielo"
            self.health = 150
        if location == "Beach":
            self.name = "Cápitan Elduin"
            self.health = 75
    def attack(self, target):
        damage = random.randint(5, 10)
        print(f"{self.name} deal {damage} damage to {target}!")
        return damage

    def take_damage(self, damage):
        self.health -= damage

    def __str__(self):
        return f"{self.name} (Health: {self.health})"
    
    
    