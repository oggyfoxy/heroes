from characters import Character, Warrior, Hunter, Mage, Healer
import random

# Game functions
def create_team():
    return {
        "warrior": Warrior("Warrior", 10),
        "hunter": Hunter("Hunter", 10),
        "mage": Mage("Mage", 10),
        "healer": Healer("Healer", 10)
    }

def create_wave(wave_num):
    if wave_num == 4:
        return [Character("Dragon", 15)]
    else:
        return [Character(f"Troll {i+1}", 5) for i in range(wave_num + 2)]

def is_wave_defeated(wave):
    return all(v.life_points <= 0 for v in wave)

def is_team_defeated(team):
    return all(h.life_points <= 0 for h in team.values())

def play_round(team, wave):
    # Heroes' attacks
    team["warrior"].attack(random.choice(wave))
    team["hunter"].attack(random.choice(wave))
    team["mage"].attack(random.choice(wave), [v for v in wave if v.life_points > 0])
    team["healer"].heal(random.choice(list(team.values())))
    team["healer"].attack(random.choice(wave))

    # Villains' attacks
    for villain in wave:
        if villain.life_points > 0:
            target = random.choice(list(team.values()))
            if villain.name == "Dragon":
                damage = random.randint(0, 6)
                target.life_points -= damage
                for hero in team.values():
                    if hero != target:
                        hero.life_points -= random.randint(0, 2)
            else:
                damage = random.randint(0, 4)
                if target.name == "Hunter":
                    damage = min(damage, 2)
                target.life_points -= damage
