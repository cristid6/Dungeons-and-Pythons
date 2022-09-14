class Enemy:
    def __init__(self, type_of):
        self.type_of = type_of
        self.life = life
        self.attack_power = attack_power
        

    def attack(self):
        pass

class Goblin(Enemy):
    def __init__(self):
        super().__init__(self, 'Goblin')
        self.life = 50
        self.attack_power = 50

class Orc(Enemy):
    def __init__(self):
        super().__init__(self, 'Orc')
        self.life = 70
        self.attack_power = 70

class Troll(Enemy):
    def __init__(self):
        super().__init__(self, 'Troll')
        self.life = 100
        self.attack_power = 100
