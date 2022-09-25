import time
from ascii import *

class TextFunctions:
    @staticmethod
    def type_answer():
        print('1. Yes\n'
              '2. No\n')

    @staticmethod
    def intro():
        print('Welcome, stranger.\n\nHere in Hinderlands, you\'ll get to fight dragons and conquer the deadliest dungeons.\n'
              'In a country where magic rules, anything is possible if you wish so.\n')
        print('Press enter to start the game or any other key to exit...')

    @staticmethod
    def choose_character():
        print('Choose a character:\n'
              '1. Warrior\n'
              '2. Wizzard\n'
              '3. Knight\n')

    @staticmethod
    def enter_name(player_character):
        print(f'Type your {player_character} name:')

    @staticmethod
    def intro_character(player_name, player_character):
        print(f'Congratulations, {player_name}! You can be a great {player_character}!\n')

    @staticmethod
    def character_message(player_character):
        if player_character == 'warrior':
            print('Warriors were high regarded in Hinderlands, as they were the only protectors\n'
                  'of common folk.\n\n'
                  'Starting the game...')
        elif player_character == 'wizard':
            print('Wizards were the scholars of Hinderlands, spreading knowledge and hope.\n'
                  'amongst the people.\n\n'
                  'Starting the game...')
        elif player_character == 'knight':
            print('Knights were the bravest.\n\n'
                  'Starting the game...')

    @staticmethod
    def please_choose():
        print('Please type only the corespondent number!')

    @staticmethod
    def choose_path(player_name):
        print(f'{player_name}, in front of you is a crossroad with 3 paths. Choose your path!\n'
              '1. To a forest\n'
              '2. To a town\n'
              '3. To a dungeon\n')

    @staticmethod
    def path_message(path):
        print(f'You chose the {path} path!\n\n'
              f'After a few days of walking, you find a chest, but maybe it\'s not what it seems to be...\n')
        time.sleep(3)
        print('Do you want to open the chest?\n')


    @staticmethod
    def loading():
        print('Loading...')

    @staticmethod
    def open_chest():
        print('The chest is opening...\n'
              'Your damage and armor values have been changed.\n'
              'Let\'s hope you can win your battle against your enemy!\n\n'
              'Be careful in the next step!\n')

    @staticmethod
    def not_open_chest():
        print('You chose not to open the chest. You just kept your damage and armor values!\n'
              'Maybe was a good choice, you will find out later!\n\n'
              'For now, we must continue our journey...\n')

    @staticmethod
    def journey_message(enemy_character):
        print(f'But wait...your journey is now in danger...a {enemy_character} is in front of you!\n'
              f'Do you think you cand kill the {enemy_character}?\n')

    @staticmethod
    def going_battle(player_character, enemy_character):
        print(f'Wow! You are certainly a brave {player_character}!\n\n'
              f'You are now going in battle with the {enemy_character}!\n\n')

    @staticmethod
    def leave_battle(enemy_character):
        print(f'Good choice! But remember, next time you can face with a stronger enemy\n'
              f'than the {enemy_character} in your journey!\n\n'
              f'You cand see a castle few miles away, go there quickly to run from the {enemy_character}!\n')

    @staticmethod
    def welcome_castle(enemy_character):
        print(f'Welcome at the castle! Here is a little problem...you just entered in the {enemy_character}\'s house!\n'
              f'You cannot run this time because the gates are closing!\n\n'
              f'Batlle with the {enemy_character}!\n')

    @staticmethod
    def intro_battle(enemy_character):
        print(f'The battle is about to begin!\n\n'
              f'You can attack the {enemy_character} once and then wait the opponent strike,\n'
              f'after that you can attack again and so on. Also you must protect yourself\n'
              f'from the {enemy_character}\'s strikes.')

    @staticmethod
    def battle():
        print('Now you are in battle! Choose if you strike first!\n')

    @staticmethod
    def end_game(player_name, player_character):
        print(f'{player_name}, this is the end of the game...you are a good {player_character}.\n'
              f'Thank you for playing!')

    @staticmethod
    def exit_game():
        print('Goodbye, stranger!')



