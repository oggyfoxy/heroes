import random
import colorama
from colorama import Fore, Style

# Initialize colorama for colored output
colorama.init()

# Define the heroes and villains
heroes = [
    {"name": "Warrior", "max_damage": 5, "health": 10},
    {"name": "Hunter", "max_damage": 3, "health": 8, "arrows": 5},
    {"name": "Mage", "max_damage": 4, "health": 6},
    {"name": "Healer", "max_damage": 1, "health": 8},
]

villains = [
    {"name": "Troll", "max_damage": 2, "health": 6},
    {"name": "Dragon", "max_damage": 8, "health": 20},
]

# Define the waves of villains
waves = [
    {"name": "Wave 1", "villains": [villains[0] for i in range(3)]},
    {"name": "Wave 2", "villains": [villains[0] for i in range(4)]},
    {"name": "Wave 3", "villains": [villains[0] for i in range(5)]},
    {"name": "Boss Wave", "villains": [villains[1]]},
]









# Define a function to get the hero's choice of target
def choose_target(heroes, villains):
    print("Choose your target:")
    for i, villain in enumerate(villains):
        print(f"{Fore.RED}{i + 1}: {villain['name']} ({villain['health']} health){Style.RESET_ALL}")
    while True:
        choice = input("> ")
        if choice.isdigit() and int(choice) in range(1, len(villains) + 1):
            return int(choice) - 1
        else:
            print(f"{Fore.YELLOW}Invalid choice. Try again.{Style.RESET_ALL}")

# Define the main game loop
def play_game():
    # Initialize the heroes' and villains' health
    for hero in heroes:
        hero["health"] = hero.get("health", 10)
    for villain in villains:
        villain["health"] = villain.get("health", 6)
    
    # Iterate over the waves of villains
    for wave in waves:
        print(f"\n{Fore.BLUE}{wave['name']}{Style.RESET_ALL}")
        # Initialize the villains' health for this wave
        for villain in wave["villains"]:
            villain["health"] = villain.get("health", 6)
        
        # Iterate over the turns in the wave
        while any(villain["health"] > 0 for villain in wave["villains"]) and any(hero["health"] > 0 for hero in heroes):
            # Print the current health of the heroes and villains
            print(f"\n{Fore.GREEN}Heroes:{Style.RESET_ALL}")
            for hero in heroes:
                print(f"{hero['name']}: {hero['health']} health")
            print(f"\n{Fore.RED}Villains:{Style.RESET_ALL}")
            for villain in wave["villains"]:
                print(f"{villain['name']}: {villain['health']} health")
            
            # Let each hero take a turn
            for hero in heroes:
                # Skip dead heroes
                if hero["health"] <= 0:
                    continue
                
                # Print the hero's name
            print(f"\n{Fore.CYAN}{hero['name']} ({hero['health']} health){Style.RESET_ALL}")
            
            # Let the hero take their action
            if hero["name"] == "Warrior":
                # Warrior chooses a target and deals damage
                target = choose_target(heroes, wave["villains"])
                damage = random.randint(1, hero["max_damage"])
                wave["villains"][target]["health"] -= damage
                print(f"{Fore.CYAN}{hero['name']} deals {damage} damage to {wave['villains'][target]['name']}.{Style.RESET_ALL}")
            
            elif hero["name"] == "Hunter":
                # Hunter chooses a target and deals damage
                target = choose_target(heroes, wave["villains"])
                if hero["arrows"] > 0:
                    damage = random.randint(1, hero["max_damage"])
                    hero["arrows"] -= 1
                else:
                    damage = 1
                wave["villains"][target]["health"] -= damage
                print(f"{Fore.CYAN}{hero['name']} deals {damage} damage to {wave['villains'][target]['name']}.{Style.RESET_ALL}")
            
            elif hero["name"] == "Mage":
                # Mage deals damage to all villains
                for villain in wave["villains"]:
                    if villain["health"] > 0:
                        damage = random.randint(1, hero["max_damage"])
                        villain["health"] -= damage
                print(f"{Fore.CYAN}{hero['name']} deals {damage} damage to all villains.{Style.RESET_ALL}")
            
            elif hero["name"] == "Healer":
                # Healer heals a hero and deals damage to a villain
                print(f"{Fore.CYAN}Choose a hero to heal:{Style.RESET_ALL}")
                for i, hero in enumerate(heroes):
                    print(f"{i + 1}: {hero['name']} ({hero['health']} health)")
                while True:
                    choice = input("> ")
                    if choice.isdigit() and int(choice) in range(1, len(heroes) + 1):
                        target = int(choice) - 1
                        heroes[target]["health"] += 2
                        if heroes[target]["health"] > 10:
                            heroes[target]["health"] = 10
                        break
                    else:
                        print(f"{Fore.YELLOW}Invalid choice. Try again.{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Choose a villain to attack:{Style.RESET_ALL}")
                for i, villain in enumerate(wave["villains"]):
                    print(f"{i + 1}: {villain['name']} ({villain['health']} health)")
                while True:
                    choice = input("> ")
                    if choice.isdigit() and int(choice) in range(1, len(wave["villains"]) + 1):
                        target = int(choice) - 1
                        damage = random.randint(1, hero["max_damage"])
                        wave["villains"][target]["health"] -= damage
                        print(f"{Fore.CYAN}{hero['name']} heals {heroes[target]['name']} for 2 health and deals {damage} damage to {wave['villains'][target]['name']}.{Style.RESET_ALL}")
                        break
                    else:
                        print(f"{Fore.YELLOW}Invalid choice. Try again.{Style.RESET_ALL}")
    
    # Check if the heroes won the wave
    if all(villain["health"] <= 0 for villain in wave["villains"]):
            print(f"{Fore.BROWN}bla bla bla{wave['name']}!{Style.RESET_ALL}")

              # Print victory message
            print(f"{Fore.GREEN}Congratulations, you have defeated the {wave['name']}!{Style.RESET_ALL}")
        
        # Check if the heroes lost the game
    if all(hero["health"] <= 0 for hero in heroes):
        print(f"\n{Fore.RED}Game Over. The heroes have been defeated.{Style.RESET_ALL}")
        return
    
    # Reset the Hunter's arrows for the next wave
    for hero in heroes:
        if hero["name"] == "Hunter":
            hero["arrows"] = 5
    
# Print victory message
print(f"\n{Fore.GREEN}Congratulations, you have defeated the Dragon and saved the kingdom!{Style.RESET_ALL}")

# Start the game
play_game()


