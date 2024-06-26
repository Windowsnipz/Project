# Loops player encounters until they die or finish each one.
import random
import time

from helpers import Zombie, printcool, get_input

death = False
zombies = 1


def encounters(protagonist):
    list_of_encounters = [1, 2, 3, 4]

    printcool(f"{protagonist.name} starts walking down the road, in search of help.")
    hours = 1
    while list_of_encounters:
        num = random.choice(list_of_encounters) #CHANGE LATER. Is set to one number for testing purposes!
        if num == 1:
            encounter1(protagonist)
        if num == 2:
            encounter2(protagonist)
        if num == 3:
            encounter3(protagonist)
        if num == 4:
            encounter4(protagonist)
        if death:
            player_death(hours, zombies)
            break
        printcool(f"{protagonist.name} continues walking down the road.")

        hours += 1
        list_of_encounters.remove(num)

    if not death:
        printcool("You made it! You won! Congratualations!", f"You survived for {hours} hour(s), and encountered {zombies} zombie(s).")
        printcool("Or did you really win?", "......")
        printcool(f"{protagonist.name} collapses on the lonely road, completely exhausted.", "This...")
        printcool("This is how you died.")




# Rosewood Medical encounter (broken collarbone?)
def encounter1(protagonist):
    global death # Declare death as a global variable
    global zombies # Declare zombies as a global variable

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
    printcool("Bodies began to fill the hallway. Bodies that weren't human.", "Horrific sounds echoed from their mouths.")

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
        printcool(f"Struggling to pry themselves free, {protagonist.name} underestimated the grip of the twisted creature.", "Give a punch or a kick?")
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
def encounter2(protagonist):
    global death # Declare death as a global variable
    global zombies
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
    printcool("It was another creature in police uniform, joined by someone else's eaten remains.", "Throw your weapon at them, or kick at their face?")
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
        printcool(f"{protagonist.name} notices they suffered a small bite on their ankle.", "Maybe kicking the zombie in the face wasn't the best idea.")

        protagonist.hurty(25)
        if protagonist.health <= 0:
            death = True
            return

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
def encounter3(protagonist):
    global death # Declare death as a global variable
    global zombies

    printcool("Meanwhile, in another part Knox County....."), time.sleep(1)

    printcool("Jorge was talking with his father in the barn.", "\"Things aren't like they used to be, Pa.\"")
    printcool("\"Like damn they aren't, Jorge.", "I'll keep doing things that have always worked for us. This farm has lasted generations.\"")

    printcool("For a moment, the two sit in silence.", "The sound of the wind died down, and the cricket chirps faded. It was dead quiet.")
    printcool("A loud crash and a blood curdling scream rumbled from the house.", "\"What the hell was that?!\" Jorge shouted.")

    printcool("The father and son run out the barn and rush over to the house.", "The building was being engulfed by a crowd of people.")
    printcool("The two of them stand in shock, trying to process the situation.", "These weren't people.")

    printcool("\"Jorge, get out of here!\" yelled Pa.", "\"I need to get your mother! Go! Now!\"")
    printcool("After briefly hesitating, Jeorge bolts away.", "Shortly after, he makes it into the nearby woods.")

    printcool("With his back against a tree, he stops and gasps for air.", "He looks up, seeing several shadows moving about the trees.")
    printcool("Nobody knows what happened to Jorge.")
    printcool("Some time passes...."), time.sleep(1)

    printcool(f"{protagonist.name} sees a farm in the distance. There's smoke coming from the property.", "Getting closer, they realize the house and barn are up in flames.")
    printcool(f"{protagonist.name} observes several burning corpses scattered about the small farm. Some are walking, and others lying still on the ground.", "They hear something mumble in the roadside ditch.")

    printcool("\"Help... is someone there...\"", f"Looking down, {protagonist.name} sees a mangled body, dressed in bloody overalls.")
    printcool("\"Get out of here...\", he whimpered with much effort. \"It's not safe.\"", f"They look away and move on. \"I'm so sorry,\" whimpered {protagonist.name} in horror.")

    printcool(f"Three corpses emerge from the trees, and start sprinting towards {protagonist.name}.", "Run or hide?")

    # number of zombies encountered increase by 3.
    zombies += 3

    run = get_input("run")

    if run: #Player runs, trips, and gets hurt by one of the zombies
        printcool(f"{protagonist.name} whips around, seeing the three ghoulish figures closing the distance.", "They make a run for it, but trip over some stones.")
        printcool(f"{protagonist.name} frantically stands up, but one of them reaches and lands a bit on the back of {protagonist.name}'s arm.")

        protagonist.hurty(25)
        if protagonist.health <= 0:
            death = True
            return
        
        printcool("They manage to slip away into the trees, losing the small pack of zombies.", f"A while later, {protagonist.name} arrives back on the road.")

    else: #Player hides, zombie sneaks up on them, and they have choices whether or not they die
        printcool(f"Slipping into the trees and running a while, {protagonist.name} hides behind a tree, bends over, and catches their breath.", "However, they still hear sounds closing in.")
        printcool(f"{protagonist.name} peeks from behind the tree, and fortunately sees only one creature.", "It's slowly hobbling in their direction.")

        printcool(f"Now approaching the tree, {protagonist.name} was ready to take action.", "Attack or shove it to the ground?")
        attack = get_input("attack")    

        if attack: #Player attacks, and is safe.
            if protagonist.weapon:
                printcool(f"{protagonist.name} lunges from behind the tree, raising their {protagonist.weapon.name}.", "They land a strong blow to the forehead, and the corpse topples over.")
                printcool(f"{protagonist.name} stands ready, staring at the creature lying still on the ground.", "The zombie isn't moving. It looks like the strike was enough.")
                printcool(f"Getting their bearings, {protagonist.name} walks back in the direction they came.", "Eventually, they emerge back on the road.")

            else: #Player dies
                printcool(f"How unfortunate. {protagonist.name} lunges from behind the tree with no weapon.", f"Unarmed, {protagonist.name} catches the creature's shoulders.")
                printcool("However, it wasn't enough.", f"{protagonist.name} underestimated the length of the zombies arms, and it grabs their face, scracthing them all over.")
                printcool(f"The zombie slowly manages to pull {protagonist.name} to the ground, and all hope was lost.")

                death = True
                return

        else: #Shove to the ground, and run off.
            printcool(f"{protagonist.name} lunges from behind the tree, charging the undead corpse.", "They give a strong shove to the chest, and it falls to the ground.")
            printcool(f"With the creature squirming on the ground, {protagonist.name} takes off.", "They rush back toward the road.")


    printcool(f"Now, there were no fiends in sight.", f"Starving and exhausted, {protagonist.name} didn't have any idea of where to go next.")


# TODO: Church encounter
def encounter4(protagonist):
    global death
    global zombies

    printcool(f"Some time later, {protagonist.name} sees a church in the distance.", "As they get closer, it seems as if the church parking lot had a single empty car.")
    printcool(f"{protagonist.name} tries the door, but it's locked.", "They walk to the back of the building, and find another locked door.")

    printcool("Glancing at one of the windows, they walk over and and take a peek inside.", "However, the blinds were shut.")
    printcool(f"{protagonist.name} gives the window a strong tug upward.", "Thankfully, someone left the window unlocked.")

    printcool(f"Quietly, {protagonist.name} glances through the window blinds.", "It was an empty church office, with a desk and bookshelf. The door was shut.")
    printcool(f"{protagonist.name} slips through the open window, and shuts it behind them.", f"Crouching under the desk, they rest for a while.")

    printcool(f"After several minutes, {protagonist.name} stands up, and walks to the office door.", "They considered whether or not snooping around the church was a good idea.")
    printcool(f"A starving {protagonist.name} carefully opens the door.", "It led to a dimly lit hallway.")

    printcool("\"There's gotta be a kitchen in here somewhere.\"", "Go right or left? down the hallway?")
    right = get_input("right")

    zombies += 2

    if right: #Zombie encounter
        printcool(f"{protagonist.name} walks down the hallway.", "They find another door, and open it. It was the actual church sanctuary room.")
        printcool(f"{protagonist.name}, walks in, seeing a lone figure kneeling at the alter.", "It looked like a man, and he was missing an arm.")

        printcool(f"\"Sir?\", {protagonist.name} mumbled, \"Are you still there?\"")
        printcool(f"He turns around to look in {protagonist.name}'s direction.", "It was too late.")
        printcool("They had already turned.", f"The creature rights itself and slowly walks toward {protagonist.name}.")
        
        printcool(f"{protagonist.name} stares at the sorry corpse walking towards them.", "Attack or leave the room?")
        attack = get_input("attack")

        if attack: #Player pushed the zombie to the ground, and gets away.
            if protagonist.weapon:
                printcool(f"{protagonist.name} twists around the creature, grabs its torso, and pulls it to the ground.", f"After a moment, {protagonist.name} pulls out their {protagonist.weapon.name} and puts the demon out of its misery.")

            else: #No weapon
                printcool(f"{protagonist.name} twists around the creature, grabs its torso, and pulls it to the ground.", f"After a moment, {protagonist.name} grabs ahold of a metal candlestick and puts the creature out of its misery.")

            printcool(f"{protagonist.name} steps out of the room, back into the hallway.", "\"AH!\"")

            printcool("They were startled by another ghoul in the hallway.", f"It grabbed {protagonist.name}'s neck. The two were struggling to see who could overpower the other.")
            protagonist.hurty(25)

            if protagonist.health <= 0:
                printcool(f"They creature gashed {protagonist.name}'s neck wide open.", "They lost consciousness, and fell to the floor.")
                death = True
                return

            printcool("This one was clearly strong.", "Give it a shove or a kick?")
            kick = get_input("kick")

            if kick: #Player gets away
                printcool(f"{protagonist.name} gave a hard kick to the knee joint.", "After a loud crack, the zombie fell to the ground.")
                printcool(f"{protagonist.name} quickly ran back to the office, and climbed out the window.", "They didn't want to be in the church any longer.")


            else: #Player dies
                printcool(f"They shove the creature to the ground, but it took {protagonist.name} with them.", "The two stuggled and squirmed on the floor.")
                printcool(f"Unfortunately, the zombie managed to get on top of {protagonist.name}.", "It was over for them. The screams eventually faded.")

                death = True
                return



        else: #Player shuts the door, and leaves the room, startled by another one in the hallway
            printcool(f"{protagonist.name} softly sidesteps out of the room, and shuts the door to the chapel.", "A moment later, they hear it thumping at the door.")
            
            printcool(f"{protagonist.name} turns around.", "\"AH!\"")
            printcool("Another zombie had managed to sneak up to them from behind.", f"It grabbed {protagonist.name}'s arm and bit down hard.")
            protagonist.hurty(25)

            if protagonist.health <= 0:
                printcool(f"{protagonist.name} jerked and managed to free their arm.", f"They sprinted back to the office. However, the damage was done. {protagonist.name} was bleeding out.")
                death = True
                return
            
            printcool(f"{protagonist.name} manages to free their arm.", "They sprint back to the office, and slam the door shut.")
            printcool("The wound was bad, but not critical.", f"{protagonist.name} finds a cloth, and ties it around the injury.")

            printcool(f"Not wanting to stay any longer, {protagonist.name} climbs out of the window.", "The church fades in the distance.")



    else: #Left, find the kitchen. 2 Zombies in the kitchen. Somehow still have a choice that gets you hurt(not die!) or not.
        zombies += 1 #Add 1 zombie to the count for this encounter. (extra zombie in the kitchen.)

        printcool(f"{protagonist.name} takes a left down the short hallway.", "They find a door, adorned with the image of a fork and knife.")
        printcool("\"This must be it,\" they mumble.", f"{protagonist.name} slowly opens the door. It was indeed the kitchen.")

        printcool("However, this kitchen was not empty.", f"Two zombies had their back to {protagonist.name}. Slowly, they turned around.")
        printcool("\"Great...\"", f"The two sprint towards {protagonist.name}. Attack or dodge?")
        attack = get_input("attack")

        if attack: #Player attacks, and gets hurt
            if protagonist.weapon:
                printcool(f"{protagonist.name} raises the {protagonist.weapon.name} and lands a good hit on one. It falls over.", f"However, the other one pounces on {protagonist.name}.")
                protagonist.hurty(25)

            else: #No weapon
                printcool(f"{protagonist.name} lunges forth, and shoves one to the ground.", "The other one was too fast. It pounces on them.")
                protagonist.hurty(25)
            
            if protagonist.health <= 0:
                printcool(f"{protagonist.name} was already too weak from their previous injuries.", "The zombie eats them alive.")
                death = True
                return
            printcool("They shove the monster off of them with much effort.", "They make a break back to the office, and hop out of the window.")
            printcool(f"Not waiting to stay any longer, {protagonist.name} climbs out of the window.", "The church fades in the distance.")

        
        else: #Player dodges, spins around, and runs back to the office.
            printcool(f"Without hesitation, {protagonist.name} ducks and slides under the two.", "They now found themselves in the back of the kitchen.")
            printcool("They quickly slip through a door that led to a large dining hall.", f"{protagonist.name} hurriedly rushes to the exit that was on the other side of the room.")
            printcool(f"Not waiting to stay any longer, {protagonist.name} bolts out the exit.", "The church fades in the distance as they get away.")

    #ending sequence not needed. Player continues along the road.




def player_death(hours=0, zombies=1):
    printcool("Uh oh, it looks like you died.", f"You survived for {hours} hour(s), and encountered {zombies} zombie(s).")