from characters.player import Player
from characters.enemy import Enemy
from characters.boss import Boss
from scenes.scene import random_location
from utils.menu import home,battle
from utils.functions import api_openai

if __name__ == "__main__":
    """
    This section is to hardcode the inputs from the user to make it easier to test
    """
    player = Player("Gale", "Poder y Conocimiento", "Mago")
    location = random_location()
    enemy = Enemy(location)
    boss = Boss(location)

    #api_openai("Haz la introducción para una epica historia,"
    # "donde un heroe principal llamado {} de caracteristica {} que en su busqueda de {}"
    # " se encuentra en {} dominada por el control de {}".format(player.name, player.build, player.objetive, location, boss.name))

    kill_count = 0

    while True:
        """
        If hero dies, Game Over
        """
        if player.health <= 0:
            print("Game Over")
            break
        home()
        option = str(input("> "))
        print(f"You found a new Enemy: {enemy.name}")
        if option == "1":
            while True:
                """
                If enemy dies, generate new enemy
                """
                if kill_count < 8:
                    if enemy.health <= 0:
                        print("Enemy killed")
                        input(">")
                        """
                        Experience for Hero
                        """
                        player.add_experience(enemy.experience)
                        enemy = Enemy(location)
                        kill_count += 1
                        print(f"Enemies killed: {kill_count}")
                        break
                else:              
                    """
                    Boss batle
                    """
                    api_openai("El {} {}, transitó los caminos de {} y se enfrentó al jefe {}"
                               " el cumplio el objetivo de {}. Continua la historia".format(player.build, player.name, location, boss.name, player.objetive))
                    location = random_location()
                    enemy = Enemy(location)
                    boss = Boss(location)
                    #api_openai("Haz una introducción en base al siguiente concepto de un juego de rol:"
                    #           " Ahora, el {} {}, se enfrentará a nuevos desafios en {}, donde deberá enfrentarse a {} "
                    #           "que controla el lugar.".format(player.build, player.name, location, boss.name))
                battle()
                option = input("> ")
                if option == "1":
                    damage = player.attack(enemy)
                    enemy.take_damage(damage)
                    enemy.attack(player)
                    player.take_damage(10)  
                elif option == 4:
                    break
                    
        elif option == 4:
            break


        
        
