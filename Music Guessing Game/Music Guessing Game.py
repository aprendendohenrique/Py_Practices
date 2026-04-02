import pygame
from time import sleep
from random import choice
from random import randint
import os


musics = ['A Kiss To Build A Dream On.mp3', 'A Man Without Love.mp3', 'Back To Black.mp3',
          'Bedroom In My Head.mp3', 'Beyond the Sea.mp3', 'Borderline.mp3',
          'Dream a Little Dream of Me.mp3', 'House of the Rising Sun.mp3', 'LOVE.mp3',
          'Notion.mp3', 'PRIDE.mp3']

pygame.init()
pygame.mixer.init()

while True:
    os.system("cls")
    print('-' * 30)
    print('Music Guesser!'.center(30))
    print('-' * 30)
    for c, m in enumerate(musics):
        print(f'{c+1} {"-"} {m}'.replace('.mp3', ''))
    msc = choice(musics)
    pygame.mixer.music.load(msc)
    pygame.mixer.music.set_volume(0.3)
    music_length = int(pygame.mixer.Sound(msc).get_length())
    while True:
        pygame.mixer.music.play(start=randint(0, music_length - 20))
        sleep(10)
        pygame.mixer.music.stop()
        player_guess = int(input('Which music do you think it is? (only numbers): '))
        if player_guess == musics.index(msc) + 1:
            print('\033[32mYou guessed it right!\033[m')
            break
        else:
            print('\033[31mYou guessed it wrong!\033[m')
            if 'Y' not in input('Do you wanna hear again? [Y/N] ').strip().upper()[0]:
                break
    if 'Y' not in input('Do you wanna play again with another music? [Y/N] ').strip().upper()[0]:
        break

