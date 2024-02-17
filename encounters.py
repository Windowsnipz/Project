# Loops player encounters until player dies :(
import random

from helpers import Zombie, printcool, random_weapon, get_input

def encounters(protagonist):
    hours = 0
    zombies = 1
    while True:
        num = random.randint(1, 5)
        if num == 1:
            encounter1(protagonist)
        if num == 2:
            encounter2(protagonist)
        if num == 3:
            encounter3(protagonist)
        if num == 4:
            encounter4(protagonist)
        if num == 5:
            encounter5(protagonist)
        if protagonist.health <= 0:
            break
        hours += 1
        zombies += 1
    player_death(hours)



def encounter1(protagonist):
    ...


def encounter2(protagonist):
    ...


def encounter3(protagonist):
    ...


def encounter4(protagonist):
    ...


def encounter5(protagonist):
    ...



def player_death(hours, zombies):
    printcool("Uh oh, it looks like you died", f"You survived for {hours} hours, and encountered {zombies} zombies.")