from characters.player import Player
from characters.enemy import Enemy
from scenes.scene import random_location
from utils.functions import api_openai

def new_enemy(type_enemy, player):
    enemy = Enemy(type_enemy, location, player.level)
    return enemy

def is_alive(entity):
    return entity.health > 0

def battle(player, enemy):
    while True:
        option = input("> ")
                    
        damage = player.attack(enemy.name)
        enemy.take_damage(damage)

        # Check if the enemy's HP is less than or equal to 0. 
        if not is_alive(enemy):
            print("Enemy killed")
            player.add_experience(enemy.experience)
            player.gold += enemy.gold
            enemy = new_enemy("Normal", player)
            return True

        damage = enemy.attack(player.name)
        player.take_damage(damage)
        
        # Check if the hero's HP. First check to end the Game.
        if not is_alive(player):
            print("Game Over")
            return False
    
if __name__ == "__main__":
    """
    This section is to hardcode the inputs from the user to make it easier to test
    """
    player = Player("Gale", "Poder y Conocimiento", "Mago")
    location = random_location()
    enemy = new_enemy("Normal", player)
    boss = new_enemy("Boss", player)
    kill_count = 0

    print(f"You found a new Enemy: {enemy.name}")


    while True:

        if player.level < 10:
            if not battle(player,enemy):
                break
            else:
                kill_count += 1
                print(f"Enemies killed: {kill_count}")
        else:
            print(f"BOSS BATTLE: YOU FOUND {boss.name}")
            if not battle(player, boss):
                break
            else:
                location = random_location()
                enemy = new_enemy("Normal", player)
                boss = new_enemy("Boss", player)

                
