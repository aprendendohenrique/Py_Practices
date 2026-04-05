from entities import player
from entities import enemies
from time import sleep
import os


def draw_ui(e_index = -1):
    print('Terminal RPG')
    print('=' * 60)
    print(f'Player: {player['name']}  HP: {p_health}/{player['health']}  Kills: {kills}')
    print('=' * 60)
    if e_index != -1:
        print(f'Enemy: {enemies[e_index]['name']}  HP: {e_health}/{enemies[e_index]['health']}')
        print('-' * 60)


kills = 0
p_health = player['health']
difficulties = ['easy', 'mid', 'hard']

while True:
    os.system('cls')
    draw_ui()
    print('Choose a difficulty:')
    print('  easy, mid, hard')
    ans = input('> ').strip().lower()
    if 'easy' in ans or 'mid' in ans or 'hard' in ans:
        e_index = difficulties.index(ans)
        e_health = enemies[e_index]['health']
        os.system('cls')
        draw_ui(e_index)

        print(f'A wild {enemies[e_index]['name']} appears!')

        while True:
            #player attack
            sleep(0.5)
            os.system('cls')
            draw_ui(e_index)
            print(f'{player['name']} hits {enemies[e_index]['name']} for {player['damage']} damage!')
            e_health -= player['damage']
            if e_health <= 0:
                print(f'{enemies[e_index]['name']} is dead')
                break

            #enemy attack
            sleep(0.5)
            os.system('cls')
            draw_ui(e_index)
            print(f'{enemies[e_index]['name']} hits {player['name']} for {enemies[e_index]['damage']} damage!')
            p_health -= enemies[e_index]['damage']
            if p_health <= 0:
                print(f'{player['name']} is dead')
                break