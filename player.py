class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def attack(self):
        pass

class Warrior(Player):
    def __init__(self):
        super().__init__(self)
        self.life = 120
        self.power = 50


class Wizard(Player):
    def __init__(self):
        super().__init__(self)
        self.life = 120
        self.power = 50

class Knight(Player):
    def __init__(self):
        super().__init__(self)
        self.life = 80
        self.power = 70


