from entities import player
from entities import enemies
from time import sleep

kills = 0
p_health = player['health']
difficulties = ['easy', 'mid', 'hard']

print('Terminal RPG')
print('='*60)
print(f'Player: {player['name']}  HP: {p_health}/{player['health']}  Kills: {kills}')
print('='*60)
while True:
    print('Choose a difficulty:')
    print('  easy, mid, hard')
    ans = input('> ').strip().lower()
    if 'easy' in ans or 'mid' in ans or 'hard' in ans:
        e_index = difficulties.index(ans)
        e_health = enemies[e_index]['health']
        print(f'Enemy: {enemies[e_index]['name']}  HP: {e_health}/{enemies[e_index]['health']}')
        print('-'*60)
        print(f'A wild {enemies[e_index]['name']} appears!')
        while True:
            sleep(0.5)
            print(f'{player['name']} hits {enemies[e_index]['name']} for {player['damage']} damage!')
            e_health -= player['damage']
            if e_health <= 0:
                print('enemy is dead')
                break
            sleep(0.5)
            print(f'{enemies[e_index]['name']} hits {player['name']} for {enemies[e_index]['damage']} damage!')
            p_health -= enemies[e_index]['damage']
            if p_health <= 0:
                print('player is dead')
                break