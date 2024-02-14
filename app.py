import random
import sys
import time
import os
import sys


from helpers import printcool, start_game
from story_paths.story_path1 import path1




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
    print()
    printcool("+--------------------------------------------+", end=None, delay=0.01)
    printcool("Welcome to Zomboid: Rosewood Rising,", "a story-based rpg based on Project Zomboid!\n\n")
    print(" ")

    if not start_game():
        sys.exit(1)




def path2():
    printcool("YEET YEET, story has not been created yet")




if __name__ == "__main__":
    main()