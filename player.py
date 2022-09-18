class Player:
    def __init__(self, name, life, power):
        self.name = name
        self.life = life
        self.power = power
        self.inventory = []

    def attack(self):
        pass

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, 120, 50)

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, 50, 120)

class Knight(Player):
    def __init__(self, name):
        super().__init__(name, 90, 80)



