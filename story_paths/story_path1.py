from helpers import Character, printcool, wait, yayornay, get_character_name, random_weapon, printgloom

# Defining story path 1
def path1():

    protagonist = get_character_name()

    printcool(f"{protagonist.name} finds themself awake, in the dim spare bedroom of their parent's apartment.", "Upon getting out of bed, they examine their surroundings.")

    #Spawn random weapon
    spawn_weapon = random_weapon()

    printcool(f"{protagonist.name} sees a {spawn_weapon.name} lying on top of the chestnut dresser.", f"Pick the {spawn_weapon.name} up?")
    choice = input()

    if yayornay(choice):
        printcool(f"{protagonist.name} decides to pick up the {spawn_weapon.name} and wield tightly, as if it were important.")
        protagonist.weapon = spawn_weapon
    else:
        printcool(f"{protagonist.name} decides to leave the {spawn_weapon.name} as is, and move on.")
    
    printcool("While coming down the stairs, all seems eerily quiet...", "Overcast weather was evident through the pale curtains of the living room windows.")
    
    printcool("However...", "The atmosphere was not the only thing that carried a pale demeanor.")

    printcool(f"Lying fetal under the coffee table was {protagonist.name}'s daughter, Emily.", "Softly call Emily's name, or sneak away?")

    choice = input(), print(), wait()
    
    if "call" in choice:
        printgloom("\"..."), printcool("Emily\"")

        printcool(f"Rolling to face {protagonist.name}, Emily's face bore tears.", "\"Something feels wrong,\" she whimpered.")

        printcool(f"\"How long have I been asleep?\" asked {protagonist.name}.", "Emily turned her eyes away, staring up at the bottom of the coffee table as if it were the ceiling.")

        printcool(f"The tears pooling in her eyes carried answers that {protagonist.name} was not getting.")

        printcool("Emily starts to emerge from under the coffee table.", "Offer to hold her, or do nothing?")

        subchoice = input(), print(), wait()

        if "hold" in subchoice:
            printcool("\"Come here, Em. Let's go outside.\"")

            printcool(f"Holding Emily in their arms, {protagonist.name} makes their way to the front door of their Kentucky home.", "Upon opening the door, they go outside.")

        else:
            printcool("Emily stands up, arms wrapped around her stomach as if she were in pain.", "\"Something feels terrible\"")

            printcool(f"{protagonist.name} and Emily make their way to the front door of their Kentucky home, and walk outside.")


    else:
        printcool(f"{protagonist.name} slips away, with an ominous feeling hanging about when they approach the kitchen.")

        printcool("Looking out of the window above the sink, it looked as gray as you would imagine.", "A very light fog accompanied the cloudy day, covering the suburban neighborhood.")