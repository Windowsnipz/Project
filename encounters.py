# Loops player encounters until player dies :(
import random
import time

from helpers import Zombie, printcool, random_weapon, get_input

death = False

def encounters(protagonist):
    printcool(f"{protagonist.name} starts walking down the road, in search of help.")
    hours = 1
    zombies = 1
    while True:
        num = random.randint(2, 2) #CHANGE LATER. Is set to one number for testing purposes!
        if num == 1:
            encounter1(protagonist, zombies)
        if num == 2:
            encounter2(protagonist, zombies)
        if num == 3:
            encounter3(protagonist, zombies)
        if num == 4:
            encounter4(protagonist, zombies)
        if num == 5:
            encounter5(protagonist, zombies)
        if death:
            break
        printcool(f"{protagonist.name} continues walking down the road.")
        hours += 1
    player_death(hours, zombies)




# Rosewood Medical encounter (broken collarbone?)
def encounter1(protagonist, zombies):
    global death # Declare death as a global variable

    printcool("Meanwhile, in another part of town....."), time.sleep(1)
    printcool("Noah was squirming in the doctor's office of Rosewood Medical.", "\"I knew I shouldn't have gone skiing today.\"")

    printcool("\"Don't put too much pressure on yourself. This break will heal on its own,\" muttered the doctor.", "His lips curled, and he started to sniffle.")

    printcool("\"What's wrong?\" asked the doctor, \"I thought you said there wasn't much pain?\"")
    printcool("\"You don't understand,\" he grumbled.", "\"There's no possible way I can afford the medical bill.\"")

    printcool("\"I'm sorry, sir, but we can't do anything about that at the moment.", "You should be focusing on getting better.\"")
    printcool("Noah was discharged, and plopped into a seat in the waiting room.", "\"I cant believe I went to the top of the mountain. I'm just a beginner!\"")

    printcool(f"{protagonist.name} burst through the doors of the clinic.", "\"HELP! HELP ME! There's something going on out there!\"")
    printcool("The shocked receptionist stared at them, mouth agape.", "\"What do you mean? Are you hurt?\"")

    printcool("A loud crash resounded from the back of the clinic, followed by a scream.", "\"Hey!! What's going on?!\"")
    printcool("Bodies begain to fill the hallway. Bodies that weren't human.", "Horrific sounds echoed from their mouths.")

    # number of zombies encountered increase by 10.
    zombies += 10

    printcool("\"You have got to be kidding me!\" Noah exclaimed.", "\"Just eat me. I've had enough...\"")
    printcool(f"{protagonist.name} started to panic.", "Fight or run away?")
    fight = get_input("fight")

    if fight: #fight, but get hurt. If fight again, you ded.
        if protagonist.weapon:
            printcool(f"{protagonist.name} tries to land a strike on an incoming zombie.", f"However, the {protagonist.weapon.name} wan't much help.")
            printcool(f"Another one came from behind and managed to scratch {protagonist.name}'s neck.")
            protagonist.hurty(25)

            if protagonist.health <= 0:
                death = True
                return
            
            #still alive, manage to get away
            printcool(f"{protagonist.name}'s panic rose to a new level.", "Run or stand your ground?")
            run = get_input("run")

            if run: # player runs away
                printcool(f"In an attempt to get away, {protagonist.name} runs out the door.", "They round the corner of the building and run down the street for a while.")
            
            else: #Player dies
                printcool(f"Digging their heels into the ground, {protagonist.name} is ready to fight off the horde.", "However, the crowd closes in on them, and they are overwhelmed.")
                printcool(f"The screams of {protagonist.name} begin to fade, and their name is added to the list of the undead.")
                death = True
                return

        else: #No weapon
            printcool(f"{protagonist.name} tries to fight off one with their bare hands.", "They soon realized that it was not very effective.")
            printcool(f"The crowd closes in on them, and {protagonist.name} is overwhelmed.")
            death = True
            return

    else: #run out the door, a zombie catches player by the shirt. 2 choices, one you get hurt, one you don't.
        printcool(f"{protagonist.name} bolts out the door, ready to make a run for it.", "However, one of the undead grabs them by the back of their shirt.")
        printcool(f"Struggling to pry themselves free, {protagonist.name} underestimated the grip of the twist creature.", "Give a punch or a kick?")
        kick = get_input("kick")

        if kick: #Break free with no harm and get away
            printcool(f"{protagonist.name} spins around and gives a leg sweep in one fluid motion.", f"The zombie falls to the ground, and {protagonist.name} is able to get away.")
            printcool("Rounding a corner, they continue to run down the street for a while.")

        else: #player gets hurt, but gets away
            printcool(f"{protagonist.name} turns and throws a punch.", "Unfortanetly, their fist land on an exposed jaw, cutting their knuckles.")
            protagonist.hurty(25)

            if protagonist.health <= 0:
                death = True
                return
            printcool(f"After knocking the creature to the ground, {protagonist.name} sprints away.", "They round the corner of a building and jog down the street for a while.")



    printcool("As some time passes, they slow down their pace to catch their breath.")




# Police car encounter
def encounter2(protagonist, zombies):
    global death # Declare death as a global variable
    zed = Zombie()

    printcool("Some time passes...."), time.sleep(1)
    printcool(f"{protagonist.name} sees two police cars in the distance, blocking the road.", "As they close the distance, they notice a single officer sitting in one of the cruisers.")

    printcool("It lookes as if they were dozing off in the driver's seat.", f"{protagonist.name} approaches to tap on the glass.")
    printcool("\"Officer? I need your help. I don't understand what's going on.\"","The policeman's head snaps up, and he jerks his face toward the window.")

    printcool("It was too late. His eyes were empty, and blood covered his face.", f"The corpse began to shake the car, banging on the window facing {protagonist.name}.")
    printcool("\"Oh my god...\"", f"{protagonist.name}'s mind was filled with fear and dread.")

    # number of zombies encountered increase by 2.
    zombies += 2

    printcool(f"Suddenly, a hand came from under the cruiser, and grabbed {protagonist.name} by the ankle.", "They fell backwards, able to see what was previously hidden underneath the car.")
    printcool("It was another creature in police uniform, joined by someone else's mangled remains.", "Throw your weapon at them, or kick at their face?")
    throw = get_input("throw")

    if throw:
        
        if protagonist.weapon: #Player throws their weapon, but retrieves it at the end.
            printcool(f"{protagonist.name} throws the {protagonist.weapon.name} at the undead corpse.", f"It hit them square in the face, and they released their grip on {protagonist.name}.")
            zed.hurty(protagonist.weapon.damage) #damage the zombie

            printcool("They stand up, quickly regaining their footing.")

            if zed.is_dead(): #pick weapon back up
                printcool("The creature lies motionless on the ground.", f"{protagonist.name} carefully walks over and retrieves their {protagonist.weapon.name}.")

                
            else: #zombie not dead, and it crawls out. Two choices, one kills it, one you die.
                printcool(f"The attack stunned it enough to let go of {protagonist.name}, but the monster kept advancing.", "It crawled out from under the vehicle, and stands up.")
                printcool(f"{protagonist.name} was on the verge of shock. The zombie lunged at them.", "Shove them away, or give a punch?")
                shove = get_input("shove")

                if shove: #Player shoves zed to ground, grabs weapon, and finishes it off.
                    printcool(f"{protagonist.name} catches it by the shoulders and shoves it to the ground.", f"They run over and grab the {protagonist.weapon.name}, which was resting on the ground near the cruiser.")
                    printcool("With the weapon in hand, they walk back over to the corpse wriggling on the ground.", f"{protagonist.name} gave a fatal blow, and the nightmare was over.")

                else: #player was not a professional boxer, and dies.
                    printcool(f"It was evident that {protagonist.name} did not have a career in professional boxing.", "The creature caught the fist in their mouth and crunched down hard.")
                    printcool("\"AAH!\"", f"The zombie managed to pull {protagonist.name} to the ground, and it was over for them.")

                    death = True
                    return


        else: #No weapon, suffer a bite
            printcool(f"Unfortunately, {protagonist.name} was not equipped with a weapon for self-defence.", f"The zombie bit a chunk of flesh out of {protagonist.name}'s leg.")

            protagonist.hurty(25)
            if protagonist.health <= 0:
                death = True
                return

            printcool(f"{protagonist.name} manage to squirm away, with blood running from their leg.", "They hobble away as fast as they can.")

    else: #Kick at their face
        printcool(f"{protagonist.name} throws a strong heel to the creature's face.", f"It softens its grip, and {protagonist.name} prys themselves free.")
        printcool("The zombie still contiues to crawl towards them.", "Run away or give it a strong heel to the head?")
        run = get_input("run")

        if run: #Player runs away
            printcool(f"{protagonist.name} starts to sprint away.")

        else: #Player stomps on the head, but gets scratched
            printcool(f"In a nervous panic, {protagonist.name} gives a series of stomps to the zombie's head, finishing it off.")
            printcool(f"{protagonist.name} raises their leg slowly, looking at the blood pouring from their ankle.", f"It seems {protagonist.name} suffered a large scratch.")

            protagonist.hurty(25)
            if protagonist.health <= 0:
                death = True
                return

    #TODO: ending the scenes, tying them all together
    printcool(f"As {protagonist.name} flees the scene, the thumping of the one left in the car began to fade.", "After a while, they recollect on the events and sob.")



# Farmboys encounter ("Things aren't like they used to be.")
def encounter3(protagonist, zombies):
    printcool("Meanwhile, in another part Knox County....."), time.sleep(1)

    printcool("Jorge was talking with his father in the barn.", "\"Things aren't like they used to be, Pa.\"")
    printcool("\"Like damn they aren't, Jorge.", "I'll keep doing things that have always worked for us.\"")

    printcool("For a moment, the two sit in silence.", "The sound of the wind died down, and the cricket chirps faded. It was dead quiet.")
    printcool("A loud crash and a blood curdling scream rumbled from the house.", "\"What the hell was that?!\" Jorge shouted.")

    printcool("The father and son run out the barn and rush over to the house.", "The building was being engulfed by a crowd of people.")
    printcool("The two of them stand in shock, trying to process the situation.", "These weren't people.")

    printcool("\"Jorge, get out of here!\"yelled Pa.", "\"I have to run in and save your mother! Go! Now!!\"")
    printcool("After briefly hesitating, Jeorge bolts away", "Shortly after, he makes it into the nearby woods.")

    printcool("With his back against a tree, he stops to catch his breath.", "He looks up, seeing several shadows moving about the trees.")
    printcool("Nobody knows whatever happened to Jorge.")
    printcool("Some time passes...."), time.sleep(1)

    printcool(f"{protagonist.name} sees a farm in the distance. There's smoke coming from the property.", "Getting closer, they realize the house and barn are up in flames.")
    printcool(f"{protagonist.name} observes several burning corpses scattered about the small farm. Some are walking, and others lying still on the ground.", "They hear something mumble in the roadside ditch.")

    printcool("\"Help... is someone there...\"", f"Looking down, {protagonist.name} sees a mangled body, dressed in bloody overalls.")
    printcool("\"Get out of here...\", he whimpered with much effort. \"It's not safe.\"", f"{protagonist.name} looks away and moves on. \"I'm  sorry.\"")


# TODO: Church encounter(?)
def encounter4(protagonist, zombies):
    ...

# TODO: encounter prompt
def encounter5(protagonist, zombies):
    ...



def player_death(hours=0, zombies=1):
    printcool("Uh oh, it looks like you died.", f"You survived for {hours} hour(s), and encountered {zombies} zombie(s).")