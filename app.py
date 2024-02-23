import random
import sys
import sys

from helpers import printcool, start_game
from story_paths.path1 import path1


def main():

    title_screen()

    # Seed random number generator
    random.seed()

    path1()


# Title screen/menu of the game where you start
def title_screen():
    print()
    printcool("+--------------------------------------------+", end=None, delay=0.01)
    printcool("Welcome to Zomboid: Rosewood Rising,", "a story-based rpg based on Project Zomboid!", middle_delay=0)

    if not start_game():
        sys.exit(1)


if __name__ == "__main__":
    main()