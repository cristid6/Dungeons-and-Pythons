import random
import time
import os

from player import *
from enemy import *

class GameFunctions:
    @staticmethod
    def random_damage():
        damage_value = random.randint(1, 80)
        return damage_value

    @staticmethod
    def random_armor():
        armor_value = random.randint(1, 80)
        return armor_value

    @staticmethod
    def random_character():
        enemy_list = ['goblin', 'orc', 'troll']
        enemy_index = random.randint(0,len(enemy_list)-1)
        return enemy_list[enemy_index]

    @staticmethod
    def random_enemy(enemy_character):
        if enemy_character == 'goblin':
            enemy = Goblin()
        elif enemy_character == 'orc':
            enemy = Orc()
        else:
            enemy = Troll()
        return enemy

    @staticmethod
    def battle_1(player, enemy):
        try:
            i = 1
            while player.life > 0 and enemy.life > 0:
                os.system('cls')
                enemy.life = enemy.life - i - player.weapon/player.life - player.power/player.life
                player.power = player.power/i
                print(f'After your strike {enemy.type_of}\'s life is {enemy.life} %.')
                time.sleep(1)
                if enemy.life  < 0:
                    print(f'Congratulations {player.name}! You won!')
                    break
                player.life = player.armor - enemy.attack_power/random.randint(i, int(round(enemy.life)))
                player.armor = random.randint(i, int(round(enemy.life)))
                print('Your armor is charging..')
                print(f'After {enemy.type_of}\'s strike your life is {player.life} %.')
                time.sleep(1)
                if player.life > enemy.life:
                    print(f'Good strike, {player.name}!')
                else:
                    print(f'Good strike but also the {enemy.type_of} hitted you!')
                time.sleep(2)
                i += 1
                if player.life < 0:
                    print(f'The {enemy.type_of} defeated you!')
                    break
        except Exception:
            if player.life > enemy.life:
                print(f'The {enemy.type_of} ran out. You won!')
            else:
                print(f'You are tired and you cannot win! The {enemy.type_of} beated you!')
        return player.life, enemy.life



    @staticmethod
    def battle_2(player, enemy):
        try:
            i = 1
            while player.life > 0 and enemy.life > 0:
                os.system('cls')
                player.life = player.armor - enemy.attack_power/random.randint(i, int(round(enemy.life)))
                player.armor = random.randint(i, int(round(enemy.life)))
                print(f'After {enemy.type_of}\'s strike your life is {player.life} %.')
                time.sleep(1)
                if player.life < 0:
                    print(f'The {enemy.type_of} defeated you!')
                    break
                enemy.life = enemy.life - i - player.weapon/(i*random.randint(i, int(round(player.life)))) - player.power/(random.randint(i, int(round(player.life))))
                player.power = player.power/i
                print('Your armor is charging..')
                print(f'After your strike {enemy.type_of}\'s life is {enemy.life} %.')
                time.sleep(1)
                if enemy.life  < 0:
                    print(f'Congratulations {player.name}! You won!')
                    break
                if player.life > enemy.life:
                    print(f'Good strike, {player.name}!')
                else:
                    print(f'Good strike but also the {enemy.type_of} hitted you!')
                time.sleep(2)
                i += 1
        except Exception:
            if player.life > enemy.life:
                print(f'The {enemy.type_of} ran out. You won!')
            else:
                print(f'You are tired and you cannot win! The {enemy.type_of} beated you!')
        return player.life, enemy.life




