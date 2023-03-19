import random

class Character:
    def __init__(self, name, life_points):
        self.name = name
        self.life_points = life_points

class Warrior(Character):
    def attack(self, target):
        damage = random.randint(0, 5)
        target.life_points -= damage

class Hunter(Character):
    def __init__(self, name, life_points, arrows=5):
        super().__init__(name, life_points)
        self.arrows = arrows

    def attack(self, target):
        if self.arrows > 0:
            damage = random.randint(0, 3)
            self.arrows -= 1
        else:
            damage = random.randint(0, 1)
        target.life_points -= damage

class Mage(Character):
    def attack(self, target, other_targets):
        damage = random.randint(0, 4)
        target.life_points -= damage

        for other_target in other_targets:
            other_damage = random.randint(0, 2)
            other_target.life_points -= other_damage

class Healer(Character):
    def heal(self, target):
        healing = 2
        target.life_points += healing

    def attack(self, target):
        damage = random.randint(0, 1)
        target.life_points -= damage