import random
import sys
import time
import os
import sys

# Add the 'story_paths' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'story_paths'))

from helpers import printcool, start_game
from story_path1 import path1

# Character object
class Character:
    def __init__(self, name):
        self._name = name
        self.health = 100
        self.weapon = None

    def hurty(self, damage_amount):
        self.health -= damage_amount

    def heal(self, restore_amount):
        self.health += restore_amount

    @property
    def name(self):
        return self._name

# Weapon object
class Weapon:
    def __init__(self, name, damage):
        self.weapon_name = name
        self.damage = damage

    @property
    def name(self):
        return self.weapon_name




def main():

    title_screen()

    # Seed random number generator
    random.seed()

    #
    num = random.randint(1,2)
    path1()
    #if num == 1:
       # path1()
    #if num == 2:
       # path2()


# Title screen/menu of the game where you start
def title_screen():
    # Welcome message
    printcool("+------------------+\n\n")
    printcool("Welcome to Project Zombois,\na text-based adventure game based on the game Project Zomboid!\n\n")
    printcool("+------------------+\n\n\n")

    if not start_game():
        sys.exit(1)




def path2():
    printcool("YEET YEET, story has not been created yet")




if __name__ == "__main__":
    main()