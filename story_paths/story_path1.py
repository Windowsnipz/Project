from helpers import Character, printcool, wait, yayornay, get_character_name

# Defining story path 1
def path1():

    protagonist = get_character_name()

    print("\n\n")
    wait()
    printcool(f"{protagonist.name} finds themself awake, in the dim spare bedroom of their parent's apartment.")
    wait()
    printcool("Upon getting out of bed, they examine their surroundings.\n\n")
    wait()

    #Spawn random weapon
    spawn_weapon = random_weapon()

    printcool(f"{protagonist.name} sees a {spawn_weapon.name} lying on top of the chestnut dresser.\n")
    wait()
    printcool(f"Pick the {spawn_weapon.name} up?\n")
    choice = input()
    print()
    wait()
    if yayornay(choice):
        printcool(f"{protagonist.name} decides to pick up the {spawn_weapon.name} and wield tightly, as if it were important.\n")
        protagonist.weapon = spawn_weapon
    else:
        printcool(f"{protagonist.name} decides to leave the {spawn_weapon.name} as is, and move on.\n")
    wait()
    printcool(f"While coming down the stairs, all seems eerily quiet..."), wait()
    printcool(f"Overcast weather was evident through the pale curtains of the living room windows.\n"), wait()
    printcool("However..."), wait(), printcool("The atmosphere was not the only thing that carried a pale demeanor.\n"), wait()
    printcool(f"Lying fetal under the coffee table was {protagonist.name}'s daughter, Emily."), wait()
    printcool(f"Softly call Emily's name, or sneak away?\n")
    choice = input()
    print(), wait()
    if "call" in choice:
        printgloom("\"..."), wait(), printcool("Emily\""), wait()
        printcool(f"Rolling to face {protagonist.name}, Emily's face bore tears.\n"), wait()
        printcool("\"Something feels wrong,\" she whimpered.\n"), wait()
        printcool(f"\"How long have I been asleep?\" asked {protagonist.name}."), wait()
        printcool("Emily turned her eyes away, staring up at the bottom of the coffee table as if it were the ceiling."), wait()
        printcool(f"The tears pooling in her eyes carried answers that {protagonist.name} was not getting.\n"), wait()
        printcool("Emily starts to emerge from under the coffee table."), wait()
        printcool("Offer to hold her, or do nothing?\n")
        subchoice = input()
        print(), wait()
        if "hold" in subchoice:
            printcool("\"Come here, Em. Let's go outside.\""), wait()
            printcool(f"Holding Emily in their arms, {protagonist.name} makes their way to the front door of their Kentucky home."), wait()
            printcool("Upon opening the door, they go outside.")
        else:
            printcool("Emily stands up, arms wrapped around her stomach as if she were in pain."), wait()
            printcool("\"Something feels terrible\"\n"), wait()
            printcool(f"{protagonist.name} and Emily make their way to the front door of their Kentucky home, and walk outside.\n"), wait()


    else:
        printcool(f"{protagonist.name} slips away, with an ominous feeling hanging about when they approach the kitchen.\n"), wait()
        printcool("Looking out of the window above the sink, it looked as gray as you would imagine."), wait()
        printcool("A very light fog accompanied the cloudy day, covering the suburban neighborhood.\n"), wait()