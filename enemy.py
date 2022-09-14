class Enemy:
    def __init__(self, type_of, life, attack_power):
        self.type_of = type_of
        self.life = life
        self.attack_power = attack_power
        

    def attack(self):
        pass

class Goblin(Enemy):
    def __init__(self):
        super().__init__('Goblin', 50, 50)

class Orc(Enemy):
    def __init__(self):
        super().__init__('Orc', 70, 70)

class Troll(Enemy):
    def __init__(self):
        super().__init__('Troll', 100, 100)

