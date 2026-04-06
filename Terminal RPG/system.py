from entities import player
from entities import enemies
from time import sleep
import os
import inventory


def draw_ui(e_index = -1):
    print('\033[34mTerminal RPG\033[m')
    print('=' * 60)
    print(f'Player: \033[33m{player['name']}\033[m  HP: {p_health}/{player['health']}  Kills: {kills}')
    print('=' * 60)
    if e_index != -1:
        print(f'Enemy: \033[31m{enemies[e_index]['name']}\033[m  HP: {e_health}/{enemies[e_index]['health']}')
        print('-' * 60)


kills = 0
p_health = player['health']
difficulties = ['easy', 'mid', 'hard']

while True:
    os.system('cls')
    draw_ui()
    if p_health <= 0:
        print('You died')
        break
    print('1 - See inventory\n2 - Shop\n3 - Fight\n4 - Exit')
    opt = input('> ').strip().lower()
    if '1' == opt:
        # See inventory
        if len(inventory.items) != 0:
            for c, i in enumerate(inventory.items.items()):
                print(f' - {i[0]}: {i[1]}')
        else:
            print('You have no items')
        input('Press enter to exit: ').strip().lower()
    elif '2' == opt:
        while True:
            os.system('cls')
            draw_ui()
            print('-'*30)
            print('Shop items'.center(30))
            print('-' * 30)
            print('1 - Heal 100 HP (10 coins)\n2 - Increase 20 Max HP (15 coins)\n3 - Increase 5 damage (15 coins)\n4 - Exit')
            l_coins = -1
            try:
                l_coins = inventory.items['coins']
                print(f'your coins: {l_coins}')
            except:
                print('your coins: 0')
            buy_opt = input('> ').strip()
            if '1' == buy_opt:
                if l_coins >= 10:
                    p_health += 100
                    if p_health > player['health']:
                        p_health = player['health']
                    l_coins -= 10
                    inventory.items['coins'] = l_coins
                else:
                    print('\033[33mYou do not have enough coins\033[m')
                    sleep(2)
            elif '2' == buy_opt:
                if l_coins >= 10:
                    player['health'] += 20
                    l_coins -= 15
                    inventory.items['coins'] = l_coins
                else:
                    print('\033[33mYou do not have enough coins\033[m')
                    sleep(2)
            elif '3' == buy_opt:
                if l_coins >= 10:
                    player['damage'] += 5
                    l_coins -= 15
                    inventory.items['coins'] = l_coins
                else:
                    print('\033[33mYou do not have enough coins\033[m')
                    sleep(2)
            elif '4' == buy_opt:
                break
            else:
                print('\033[33mPlease type a valid option\033[m')
                sleep(2)
    elif '3' == opt:
        # Fight
        print('Choose a difficulty:')
        print('  \033[32measy\033[m, \033[33mmid\033[m, \033[31mhard\033[m')
        ans = input('> ').strip().lower()
        if 'easy' in ans or 'mid' in ans or 'hard' in ans:
            e_index = difficulties.index(ans)
            e_health = enemies[e_index]['health']
            os.system('cls')
            draw_ui(e_index)
            txt = f'A wild {enemies[e_index]['name']} appears!\n'
            print(txt)
            while True:
                #player attack
                sleep(0.5)
                os.system('cls')
                draw_ui(e_index)
                txt += f'\033[33m{player['name']}\033[m hits \033[31m{enemies[e_index]['name']}\033[m for \033[33m{player['damage']} damage!\033[m\n'
                print(txt)
                e_health -= player['damage']
                if e_health <= 0:
                    os.system('cls')
                    draw_ui(e_index)
                    print(txt)
                    print(f'{enemies[e_index]['name']} is dead')
                    for i in enemies[e_index]['drops'].items():
                        inventory.add_item(i)
                        print(f'The enemy dropped {i[1]} {i[0]}')
                    sleep(2.5)
                    break

                #enemy attack
                sleep(0.5)
                os.system('cls')
                draw_ui(e_index)
                txt += f'\033[31m{enemies[e_index]['name']}\033[m hits \033[33m{player['name']}\033[m for \033[31m{enemies[e_index]['damage']} damage!\033[m\n'
                print(txt)
                p_health -= enemies[e_index]['damage']
                if p_health <= 0:
                    os.system('cls')
                    draw_ui(e_index)
                    print(txt)
                    sleep(2.5)
                    break
    elif '4' == opt:
        break
    else:
        print('\033[33mPlease type a valid option\033[m')