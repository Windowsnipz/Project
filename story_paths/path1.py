from helpers import Zombie, printcool, get_character_name, random_weapon, printgloom, get_input

# Defining story path 1
def path1():

    protagonist = get_character_name()

    printcool(f"{protagonist.name} finds themself awake, in the dim spare bedroom of their Kentucky home.", "Upon getting out of bed, they examine their surroundings.")

    #Spawn random weapon
    spawn_weapon = random_weapon()

    printcool(f"{protagonist.name} sees a {spawn_weapon.name} lying on top of the chestnut dresser.", f"Pick the {spawn_weapon.name} up?")

    if get_input(type="bool"):

        printcool(f"{protagonist.name} decides to pick up the {spawn_weapon.name} and wield tightly, as if it were important.")
        protagonist.weapon = spawn_weapon

    else:
        printcool(f"{protagonist.name} decides to leave the {spawn_weapon.name} as is, and move on.")
    
    printcool("While coming down the stairs, all seems eerily quiet...", "Overcast weather was evident through the pale curtains of the living room windows.")
    
    printcool("However...", "The atmosphere was not the only thing that carried a pale demeanor.")

    printcool(f"Lying fetal under the coffee table was {protagonist.name}'s daughter, Emily.", "Softly call Emily's name, or sneak away?")

    # get_input() returns a boolean value
    choice = get_input("call")
    
    if choice:

        emily = True

        printgloom("\"..."), printcool("Emily\"")

        printcool(f"Rolling to face {protagonist.name}, Emily's face bore tears.", "\"Something feels wrong,\" she whimpered.")

        printcool(f"\"How long have I been asleep?\" asked {protagonist.name}.", "Emily turned her eyes away, staring up at the bottom of the coffee table as if it were the ceiling.")

        printcool(f"The tears pooling in her eyes carried answers that {protagonist.name} was not getting.")

        printcool("Emily starts to emerge from under the coffee table.", "Offer to hold her, or do nothing?")

        subchoice = get_input("hold")

        if subchoice:
            hold = True
            printcool("\"Come here, Em. Let's go outside.\"")

            printcool(f"Holding Emily in their arms, {protagonist.name} makes their way to the front door of their house.", "Upon opening the door, they go outside.")

        else:
            printcool("Emily stands up, arms wrapped around her stomach as if she were in pain.", "\"Something feels terrible\"")

            printcool(f"{protagonist.name} and Emily make their way to the front door of their Kentucky home, and walk outside.")

        printcool(f"The heavy air instantly sent chills up {protagonist.name}'s spine.", "Something did not feel right with the setting...")

        if hold:
            printcool("Suddenly, Emily's body went limp.", f"{protagonist.name} felt the weight shift, and lowered her to the ground.")

            printcool("\"Emily!\"", "Something was wrong. Her body was unnaturally cold.")

        else:
            printcool(f"A sudden thud startled {protagonist.name}.", "Looking back, they saw Emily who'd just fallen to the ground, convulsing unconrallably.")

            printcool(f"\"Emily!\"", "Indeed, something was horribly wrong.")

        emily_encounter1(protagonist)

    else:
        printcool(f"{protagonist.name} slips away, with an ominous feeling hanging about when they approach the kitchen.")

        printcool("Looking out of the window above the sink, it looked as gray as you would imagine.", "A very light fog accompanied the cloudy day, covering the suburban neighborhood.")

        printcool(f"Sneaking out of the front door, {protagonist.name} finds themself encapsulated in the gloomy weather.", "The heavy air sent chills up their spine.")






def emily_encounter1(protagonist):
    emily = Zombie()

    printcool("Suddenly, Emily looks up at the sky.", "Her eyes are bloodshot and glazed over.")

    printcool("It all happened so fast.", f"She stood up so quickly, {protagonist.name} couldn't believe it.")

    printcool(f"Emily lunges at {protagonist.name}, demonic sounds echoing from her throat.", "Defend yourself, or do nothing?")

    choice = get_input("defend")

    if choice:
        printcool(f"{protagonist.name} defends themself, and takes out the {protagonist.weapon.name}.")