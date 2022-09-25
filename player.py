from gameFunctions import GameFunctions

class Player:
    def __init__(self, name, life, power, weapon, armor):
        self.name = name
        self.life = life
        self.power = power
        self.weapon = weapon
        self.armor = armor

class Warrior(Player):
    def __init__(self):
        super().__init__('warrior', 100, 50, 70, 90)

class Wizard(Player):
    def __init__(self):
        super().__init__('wizard', 100, 80, 40, 30)

class Knight(Player):
    def __init__(self):
        super().__init__('knight', 100, 30, 50, 70)

