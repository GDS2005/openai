from characters.player import Player
from characters.enemy import Enemy
from characters.boss import Boss
from scenes.scene import random_location
from utils.functions import api_openai

if __name__ == "__main__":
    """
    This section is to hardcode the inputs from the user to make it easier to test
    """
    player = Player("Gale", "Poder y Conocimiento", "Mago")
    location = random_location()
    enemy = Enemy(location)
    boss = Boss(location)
    kill_count = 0

    print(f"You found a new Enemy: {enemy.name}")

    while True:
        option = input("> ")
        
        damage = player.attack(enemy.name)
        enemy.take_damage(damage)

        # Check if the enemy's HP is less than or equal to 0. 
        if enemy.health <= 0:
            print("Enemy killed")
            """
            Experience for Hero
            """
            player.add_experience(enemy.experience)
            enemy = Enemy(location)
            kill_count += 1
            print(f"Enemies killed: {kill_count}")

        damage = enemy.attack(player.name)
        player.take_damage(damage)
        
        # Check if the hero's HP. First check to end the Game.
        if player.health <= 0:
            print("Game Over")
            break

        if kill_count >= 8:
            """
            Boss Battle
            """
            print(f"BOSS BATTLE: YOU FOUND {boss.name}")
            while True:
                option = input("> ")
        
                damage = player.attack(boss.name)
                boss.take_damage(damage)

                # Check if the Boss's HP is less than or equal to 0. 
                if boss.health <= 0:
                    print("Enemy killed")
                    player.add_experience(1000)
                    location = random_location()
                    enemy = Enemy(location)
                    boss = Boss(location)
                    break

                damage = boss.attack(player.name)
                player.take_damage(damage)