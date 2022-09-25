import random

class Enemy:
    def __init__(self, type_of, life, attack_power):
        self.type_of = type_of
        self.life = life
        self.attack_power = attack_power

class Goblin(Enemy):
    def __init__(self):
        super().__init__('goblin', 100, random.randint(50, 70))

class Orc(Enemy):
    def __init__(self):
        super().__init__('orc', 100, random.randint(70, 90))

class Troll(Enemy):
    def __init__(self):
        super().__init__('troll', 100, random.randint(80, 100))



