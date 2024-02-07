import sys
import random
import time

def random_weapon():
    num = random.randint(1,3)
    if num == 1:
        weapon = Weapon("hammer", 20)
        return weapon
    if num == 2:
        weapon = Weapon("kitchen knife", 40)
        return weapon
    if num == 3:
        weapon = Weapon("machete", 60)
        return weapon


# Returns a bool based on a y or n question for player
def yayornay(response):
    if response.lower() == "y" or response.lower() == "yes":
        return True
    return False

# Starts.... the game
def start_game():
    printcool("Would you like to start the game?\n")
    start = input()
    if start.lower() == "y" or start.lower() == "yes":
        print()
        return True
    return False


# Gets character name and returns a character object
def get_character_name():
    printcool("What is the name of your lonely survivor?")
    name = input()
    name = name.title()

    # Establish the protagonist as a Character object
    protagonist = Character(name)
    return protagonist

# A 1.5 second delay for the console output
def wait():
    time.sleep(1.5)

#Prints like printcool(), but slower for a gloomy feeling.
def printgloom(text):
    for c in text:
        print(c, flush=True, end="")
        time.sleep(0.25)


# Prints out text in a cool, game-like format. Flush required to work.
def printcool(text):
    for c in text:
        print(c, flush=True, end="")
        time.sleep(0.05)
    print()