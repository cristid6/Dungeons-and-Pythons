import os
import winsound
import time
from player import *
from enemy import *
from textFunctions import TextFunctions
from gameFunctions import GameFunctions


#INTRO SCENE

winsound.PlaySound(r'Main_Menu.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
time.sleep(1)
TextFunctions.intro()
if input() == '':
    os.system('cls')
    TextFunctions.loading()
    time.sleep(3)


    os.system('cls')
    TextFunctions.choose_character()
    TextFunctions.please_choose()
    while True:
        choose_character = input()
        if choose_character == '1':
            os.system('cls')
            player = Warrior()
            player_character = player.name
            TextFunctions.enter_name(player_character)
            player_name = input()
            break
        elif choose_character == '2':
            os.system('cls')
            player = Wizard()
            player_character = player.name
            TextFunctions.enter_name(player_character)
            player_name = input()
            break
        elif choose_character == '3':
            os.system('cls')
            player = Knight()
            player_character = player.name
            TextFunctions.enter_name(player_character)
            player_name = input()
            break
        else:
            TextFunctions.please_choose()
            continue

    TextFunctions.intro_character(player_name, player_character)
    time.sleep(3)
    TextFunctions.character_message(player_character)
    time.sleep(6)


#EXPLORING SCENE

    winsound.PlaySound(r'Exploring.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
    os.system('cls')

    time.sleep(1)
    TextFunctions.choose_path(player_name)
    TextFunctions.please_choose()
    while True:
        choose_path = input()
        if choose_path == '1':
            os.system('cls')
            path = 'forest'
            break
        elif choose_path == '2':
            os.system('cls')
            path = 'town'
            break
        elif choose_path == '3':
            os.system('cls')
            path = 'dungeon'
            break
        else:
            TextFunctions.please_choose()
            continue

    TextFunctions.path_message(path)
    TextFunctions.type_answer()
    time.sleep(1)
    TextFunctions.please_choose()
    time.sleep(1)
    while True:
        choose_open = input()
        if choose_open == '1':
            os.system('cls')
            player.weapon = GameFunctions.random_damage()
            player.armor = GameFunctions.random_armor()
            TextFunctions.open_chest()
            time.sleep(8)
            break
        elif choose_open == '2':
            os.system('cls')
            TextFunctions.not_open_chest()
            time.sleep(8)
            break
        else:
            TextFunctions.please_choose()
            continue

    os.system('cls')
    enemy_character = GameFunctions.random_character()
    enemy = GameFunctions.random_enemy(enemy_character)
    TextFunctions.journey_message(enemy_character)
    TextFunctions.type_answer()
    time.sleep(1)
    TextFunctions.please_choose()
    time.sleep(1)
    while True:
        choose_kill = input()
        if choose_kill == '1':
            os.system('cls')
            TextFunctions.going_battle(player_character, enemy_character)
            time.sleep(8)
            break
        elif choose_kill == '2':
            os.system('cls')
            TextFunctions.leave_battle(enemy_character)
            time.sleep(10)
            os.system('cls')
            enemy_character = GameFunctions.random_character()
            enemy = GameFunctions.random_enemy(enemy_character)
            TextFunctions.welcome_castle(enemy_character)
            time.sleep(10)
            break
        else:
            TextFunctions.please_choose()
            continue

    os.system('cls')
    TextFunctions.intro_battle(enemy_character)
    time.sleep(8)


#BATTLE SCENE

    winsound.PlaySound(r'BattleFinal.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
    os.system('cls')

    time.sleep(1)
    TextFunctions.battle()
    TextFunctions.type_answer()
    while True:
        first_strike = input()
        if first_strike == '1':
            GameFunctions.battle_1(player, enemy)
            break
        elif first_strike == '2':
            GameFunctions.battle_2(player, enemy)
            break
        else:
            TextFunctions.please_choose()
            continue

    time.sleep(3)
    TextFunctions.end_game(player_name, player_character)
    winsound.PlaySound(None, winsound.SND_PURGE)

else:
    os.system('cls')
    TextFunctions.exit_game()
    winsound.PlaySound(None, winsound.SND_PURGE)
