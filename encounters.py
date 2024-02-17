# Loops player encounters until player dies :(
import random

from helpers import Zombie, printcool, random_weapon, get_input

def encounters(protagonist):
    hours = 0
    zombies = 1
    while True:
        num = random.randint(1, 5)
        if num == 1:
            encounter1()
        if num == 2:
            encounter2()
        if num == 3:
            encounter3()
        if num == 4:
            encounter4()
        if num == 5:
            encounter5()
        if protagonist.health <= 0:
            break
        hours += 1
        zombies += 1
    player_death(hours)



def encounter1():
    ...


def encounter2():
    ...


def encounter3():
    ...


def encounter4():
    ...


def encounter5():
    ...



def player_death(hours, zombies):
    printcool("Uh oh, it looks like you died", f"You survived for {hours} hours, and encountered {zombies} zombies.")