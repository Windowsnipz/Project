# Loops player encounters until player dies :(
import random

from helpers import Zombie, printcool, random_weapon, get_input

def encounters(protagonist):
    printcool(f"{protagonist.name} starts walking down the road, in search of help.")
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
        printcool(f"{protagonist.name} continues walking down the road.")
        hours += 1
        zombies += 1
    player_death(hours, zombies)




# Rosewood Medical encounter (broken collarbone?)
def encounter1(protagonist):
    printcool("Noah was squirming in the doctor's office of Rosewood Medical.", "\"I knew I shouldn't have gone skiing today\"")

    printcool("\"Don't put too much pressure on yourself. This break will heal on its own\" muttered the doctor.", "His lips curled, and he started to sniffle.")

    printcool("\"What's wrong?\" asked the doctor, \"I thought you said there wasn't much pain?\"")
    printcool("\"You don't understand\" he grumbled.", "\"There's no possible way I can afford the medical bill.\"")

    printcool("\"I'm sorry, sir, but we can't do anything about that at the moment.", "You should be focusing on getting better.\"")
    printcool("Noah was discharged, and plopped into a seat in the waiting room.", "\" I cant believe I went to the top of the mountain. I'm just a beginner!\"")

    printcool(f"{protagonist.name} burst through the doors of the clinic.", "\"HELP! HELP ME! There's something going on out there!\"")
    printcool("The shocked receptionist stared at them, mouth agape", "\"What do you mean? Are you hurt?\"")

    printcool("A loud crash resounded from the back of the clinic, followed by a scream", "\"Hey!! What's going on?!\"")
    printcool("Bodies begain to fill the hallway. Bodies that weren't human.", "Horrific sounds echoed from their mouths.")

    printcool("\"You have got to be kidding me!\" Noah exclaimed.", "\"Just eat me. I've had enough\"")
    printcool(f"{protagonist.name} started to panic.", "Fight or run away?")
    fight = get_input("fight")


# Police car encounter
def encounter2(protagonist):
    ...


# Farmboys encounter ("Things aren't like they used to be.")
def encounter3(protagonist):
    ...


# TODO: encounter prompt
def encounter4(protagonist):
    ...

# TODO: encounter prompt
def encounter5(protagonist):
    ...



def player_death(hours=0, zombies=1):
    printcool("Uh oh, it looks like you died.", f"You survived for {hours} hour(s), and encountered {zombies} zombie(s).")