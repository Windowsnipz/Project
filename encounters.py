# Loops player encounters until player dies :(
import random

from helpers import Zombie, printcool, random_weapon, get_input

def encounters(protagonist):
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
    player_death()



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



def player_death():
    ...