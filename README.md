# Zomboid: Rosewood Rising
#### Video Demo:  <URL HERE>
#### Description:

Welcome to my final project for CS50x! This is a command line game, inspired by the very popular Project Zomboid. Project Zomboid (PZ) is a hardcore survival game set in a zombie apocalypse. In my project, I wanted to capture this setting in a text-based adventure game! Text in this game is rendered to the terminal with a custom 'printcool' function, which can take several arguments and print dialougue in a modular format. This makes the game dialougue more readable to the user.

Zomboid: Rosewood Rising starts with a simplistic menu screen, in which the player chooses whether or not to start the game. Upon starting, the introduction to the story in path1.py is executed, and the player will be prompted to enter a name for their survivor. My get_character_name() function in helpers.py was fairly simple to implement. Basically, it makes sure that (1) the name is not empty and (2) the name does not match the list of existing characters in the story (GLOBAL_CHARACTERS list).

Afterwards, the actual introduction scenario will run. This scene will always be run at the start of the game. However, there are several decision trees the player will follow. First, the dialougue draws the user's attention to a random weapon that will spawn upon starting the game. Both the character and the weapons are python objects defined in helpers.py. Additionally, I implemented a random feature, so one of the three different weapons will spawn randomly. It is up to the player whether or not they choose to take the weapon. Choices in this game are determined by a text input by the user with the get_input() function. This function is written to get either regular text input or can be modified to get a boolean expression from the user (yes or no). It works for looking for a keyword inputted by the user. Empty responses will default to one of the prompted choices.

The character object initializes with a health attribute set to 100. This value changes along the story if the player suffers injuries, in which the hurty method will reduce the health of the user. The name property of the character object is used in formatted strings in the dialougue to return the name of the player. The character object also initializes with self.weapon = None. This value will actually change if the player decides to pick up the spawned weapon at the start of the game. The weapon object will be related to the character object in this way.

The weapon object initializes with required arguments of "name" and "damage". This object also has a name property which identically returns the name of the weapon. This can be seen in the formatted dialogue strings, calling {protagonist.weapon.name}, where 'protagonist' is a character object. The weapon object is nested within the character object if the player chooses a weapon. Making this game has helped in my understand of object-oriented programming (OOP).




# Personal Notes (delete before submission)

What will your software do? What features will it have? How will it be executed?

My game will be a text-based adventure game executed in python. The game will feature an engaging story, random elements, and text inputs from the user.

What new skills will you need to acquire? What topics will you need to research?

I'll need to gain skills in game development and making a functional appilication in python.

In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome? 
1. A good outcome for my project is a functional game that will output an interesting story, and the user can input text decisions to determine outcomes of the game
2. A better outcome would be to implement features of randomness to add more storylines and enhance replayability of the game.
3. The best outcome is to create a game with a large scope, implement multiple storylines/characters, and package the game into an executable to distribute to friends.

