#COLORAMA - FOR VISUAL COLOR CMD
from colorama import Fore,Style

def home():
    print(Style.BRIGHT + Fore.YELLOW + """

    _   .-')       ('-.       .-') _             
    ( '.( OO )_   _(  OO)     ( OO ) )            
    ,--.   ,--.)(,------.,--./ ,--,' ,--. ,--.   
    |   `.'   |  |  .---'|   \ |  |\ |  | |  |   
    |         |  |  |    |    \|  | )|  | | .-') 
    |  |'.'|  | (|  '--. |  .     |/ |  |_|( OO )
    |  |   |  |  |  .--' |  |\    |  |  | | `-' /
    |  |   |  |  |  `---.|  | \   | ('  '-'(_.-' 
    `--'   `--'  `------'`--'  `--'   `-----'    
    
    """ + Fore.WHITE + """ V 1.0
    
    1. Battle
    2. Status
    3. Shop
    4. Exit
    """)

def battle():
    print(Style.BRIGHT + Fore.BLUE + """

    ______________________________________
    1. ATK  2. BLOCK  3: POTION 4: SURREND
    ______________________________________   
                           
    """ + Fore.WHITE )