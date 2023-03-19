import pickle
from game_functions import create_team

def upgrade_phase(team):
    def upgrade_hero(hero):
        hero.life_points += 5
        print(f"{hero.name} has been upgraded. New life points: {hero.life_points}")

    print("Upgrade phase:")
    for hero in team.values():
        upgrade = input(f"Do you want to upgrade {hero.name}? (y/n): ")
        if upgrade.lower() == 'y':
            upgrade_hero(hero)

def save_game(team, wave_num):
    game_data = {'team': team, 'wave_num': wave_num}
    with open('game_data.pkl', 'wb') as f:
        pickle.dump(game_data, f)
    print("Game saved!")

def load_game():
    try:
        with open('game_data.pkl', 'rb') as f:
            game_data = pickle.load(f)
        return game_data['team'], game_data['wave_num']
    except FileNotFoundError:
        print("No saved game found.")
        return create_team(), 1
