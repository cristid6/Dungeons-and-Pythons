class Enemy:
    def __init__(self, type_of):
        self.type = type_of

    def attack(self):
        pass

class Goblin(Enemy):
    def __init__(self):
        super().__init__(self)
        self.life = 50
        self.attack_power = 50

class Orc(Enemy):
    def __init__(self):
        super().__init__(self)
        self.life = 70
        self.attack_power = 70

class Troll(Enemy):
    def __init__(self):
        super().__init__(self)
        self.life = 100
        self.attack_power = 100