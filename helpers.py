import sys
import random
import time

GLOBAL_CHARACTERS = ["Emily", "Noah"]

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

class Zombie:
    def __init__(self, health=50, damage=25):
        self.health = health
        self.damage = damage

    def hurty(self, damage_amount):
        self.health -= damage_amount

    def is_dead(self):
        return self.health <= 0

# Weapon object
class Weapon:
    def __init__(self, name, damage):
        self.weapon_name = name
        self.damage = damage

    @property
    def name(self):
        return self.weapon_name


def random_weapon():
    num = random.randint(1,3)
    if num == 1:
        weapon = Weapon("hammer", 25)
        return weapon
    if num == 2:
        weapon = Weapon("kitchen knife", 40)
        return weapon
    if num == 3:
        weapon = Weapon("machete", 60)
        return weapon


# Starts.... the game
def start_game():
    printcool("Would you like to start the game?", end=None)
    if get_input(type="bool"):
        return True
    print()
    return False


# Gets character name and returns a character object
            #TODO - Add a check for the name to make sure it's not empty, or too long.
            #TODO - Make sure name is not in GLOBAL_CHARACTERS
def get_character_name():
    while True:
        printcool("+--------------------------------------------+", end=None, delay=0.01)
        printcool("What is the name of your survivor?", end=None)
        name = input()
        printcool("\n+--------------------------------------------+", end=None, delay=0.01)
        time.sleep(1.1)
        name = name.title()
        if name not in GLOBAL_CHARACTERS:
            # Establish the protagonist as a Character object
            protagonist = Character(name)
            return protagonist
            
        printcool(f"{name} is already a character in the story. Please choose another name.", end=None)


# A 1.5 second delay for the console output
def wait():
    time.sleep(1.5)

#Prints like printcool(), but slower for a gloomy feeling.
def printgloom(text):
    for c in text:
        print(c, flush=True, end="")
        time.sleep(0.25)


# Prints out text in a cool, game-like format. Flush required to work.
def printcool(text, text2="", end="+--------------------------------------------+", delay=0.05, middle_delay=1.1):
    for c in text:
        print(c, flush=True, end="")
        time.sleep(delay)
    print()
    if text2 != "":
        time.sleep(middle_delay)
        for c in text2:
            print(c, flush=True, end="")
            time.sleep(delay)
        time.sleep(middle_delay)
        print()
    if end == None:
        print()
        return
    else:
        print()
        for c in end:
            print(c, flush=True, end="")
            time.sleep(0.01)
        print("\n")
        time.sleep(1.1)

# Gets input from the user, validates it. Is customizable for different types of input.
# TODO: Add a check for the input to make sure it's not empty.
def get_input(keyword="", type=""):
    if type == "":
        choice = input().lower()
        words = choice.split()
        if keyword.lower() in words:
            print()
            time.sleep(1.5)
            return True
        else:
            print()
            time.sleep(1.5)
            return False
    if type == "bool":
        choice = input().lower()
        if choice == "y" or choice == "yes":
            print()
            time.sleep(1.5)
            return True
        print()
        time.sleep(1.5)
        return False
    