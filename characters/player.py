import random

class Player:
    """
    STATS
    S -> Strength
    P -> Perception
    E -> Endurence
    C -> Charisma
    I -> Intelligence
    A -> Agility
    L -> Luck
    """
    def __init__(self, name, objetive, build):
        self.name = name
        self.objetive = objetive
        self.build = build
        """
        Depending of the build, this will be our stats:
        """
        self.health = 5 * 20
        self.strength = 5
        self.perception = 5
        self.endurence = 5
        self.charisma = 5
        self.intelligence = 5
        self.agility = 5
        self.luck = 5
        self.level = 1
        self.experience = 0
        self.special = 2

    def attack(self, target):
        damage = random.randint(self.strength, self.strength + 5)
        """
        Critical Chance
        """
        if random.randint(1,10) > int(self.agility / 3):
            damage = damage * 2 
            print(f"{self.name} deal {damage} CRITICAL damage to {target}!")
        else:
         print(f"{self.name} deal {damage} damage to {target}!")
        
        return damage

    def take_damage(self, damage):
        self.health -= damage

    def add_experience(self, value):
        print(f"Experience gained: {value}")
        self.experience += value
        """
        Hero level up
        """
        if self.experience > self.level * 150:
            print(f"¡{self.name} level up!")
            self.level += 1
            self.endurence += 1
            self.health = self.endurence * 20
            self.strength += 1
    
    #def __str__(self):
    #    return f"{self.name}: (Health: {self.health}) (LvL: {self.level})"
    
