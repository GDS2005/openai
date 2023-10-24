import random

class Enemy:
    def __init__(self, type ,location, level):
        self.strength = random.randint(level,level+5)
        self.perception = random.randint(level,level+5)
        self.endurence = random.randint(level,level+5)
        self.charisma = random.randint(level,level+5)
        self.intelligence = random.randint(level,level+5)
        self.agility = random.randint(level,level+5)
        self.luck = random.randint(level,level+5)
        self.level = level
        self.experience = level * 100
        self.type = type
        if self.type == "Normal":
            if location == "Forest":
                self.name = "Oso"
                self.health = self.endurence * 15
            if location == "Mountain":
                self.name = "Lobo"
                self.health = self.endurence * 20
            if location == "Beach":
                self.name = "Pirata"
                self.health = self.endurence * 15
        else:
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
        damage = random.randint(self.strength, self.strength + 5)
        """
        Critical Chance
        """
        if random.randint(1,10) < int(self.luck / 3):
            damage = damage * 2 
            print(f"{self.name} deal {damage} CRITICAL damage to {target}!")
        else:
         print(f"{self.name} deal {damage} damage to {target}!")
        
        return damage

    def take_damage(self, damage):
        self.health -= damage