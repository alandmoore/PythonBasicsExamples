"""Taco Cat Goat Cheese Pizza simulator"""

import random
from time import sleep
from itertools import cycle
from pathlib import Path

working_directory = Path(__file__).absolute().parent

PLAY_TO_SLAPS = 5

with open(working_directory / 'cards.txt') as fh:
    cardnames = [x.strip() for x in fh]

print(f"Will simulate the game to {PLAY_TO_SLAPS} slaps")
print('SPOKEN\tDRAWN')
print('------\t-----')

slaps = 0
spoken = cycle(cardnames)
while slaps < PLAY_TO_SLAPS:
    spoken_card = next(spoken)
    drawn_card = random.choice(cardnames)
    print(f'{spoken_card}\t{drawn_card}')
    if spoken_card == drawn_card:
        print('SLAP!')
        slaps += 1
    sleep(1)

print('game over!')
    
    
