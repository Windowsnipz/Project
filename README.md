# Zomboid: Rosewood Rising
#### Video Demo:  https://www.youtube.com/watch?v=5xUiFtnQ4DA&ab_channel=NoahStrickland
#### Description:

##### Game initialization
Welcome to my final project for CS50x! This is a command line game, inspired by the very popular Project Zomboid. Project Zomboid (PZ) is a hardcore survival game set in a zombie apocalypse. In my project, I wanted to capture this setting in a text-based adventure game! Text in this game is rendered to the terminal with a custom 'printcool' function, which can take several arguments and print dialougue in a modular format. This makes the game dialougue more readable to the user.

Zomboid: Rosewood Rising starts with a simplistic menu screen, in which the player chooses whether or not to start the game. Upon starting, the introduction to the story in path1.py is executed, and the player will be prompted to enter a name for their survivor. My get_character_name() function in helpers.py was fairly simple to implement. Basically, it makes sure that (1) the name is not empty and (2) the name does not match the list of existing characters in the story (GLOBAL_CHARACTERS list).

Afterwards, the actual introduction scenario will run. This scene will always be run at the start of the game. However, there are several decision trees the player will follow. First, the dialougue draws the user's attention to a random weapon that will spawn upon starting the game. Both the character and the weapons are python objects defined in helpers.py. Additionally, I implemented a random feature, so one of the three different weapons will spawn randomly. It is up to the player whether or not they choose to take the weapon. Choices in this game are determined by a text input by the user with the get_input() function. This function is written to get either regular text input or can be modified to get a boolean expression from the user (yes or no). It works for looking for a keyword inputted by the user. Empty responses will default to one of the prompted choices.

The character object initializes with a health attribute set to 100. This value changes along the story if the player suffers injuries, in which the hurty method will reduce the health of the user. The name property of the character object is used in formatted strings in the dialougue to return the name of the player. The character object also initializes with self.weapon = None. This value will actually change if the player decides to pick up the spawned weapon at the start of the game. The weapon object will be related to the character object in this way.

The weapon object initializes with required arguments of "name" and "damage". This object also has a name property which identically returns the name of the weapon. This can be seen in the formatted dialogue strings, calling {protagonist.weapon.name}, where 'protagonist' is a character object. The weapon object is nested within the character object if the player chooses a weapon. Making this game has helped in my understand of object-oriented programming (OOP).

There is also a zombie object, which is functionally similar to the character object. I only implemented it a few times in the story, just to add more OOP practice to my project. The zombie also has health and damage values.

##### Story Design
Ultimately, my goal with the story design was to capture the hardcore survival aspect of Project Zomboid.

The story is stuctured in a way that the player cycles through four different encounters/scenarios at random. Within these encounters, players have a variety of choices they make that impacts whether they survive, get hurt, or die. Other than getting input from the player, these encounters were all written by myself and feature an engaging story. Variables like hours survived and zombies encountered will be updated and stored accordingly. If the character's health reaches zero, the player_death function will execute displaying how long they survived (in hours) and how many zombies they encountered on their playthrough. If the player successfully survives the introduction and all four encounters, a special surprise is presented to them at the end 😊.

##### Final Thoughts
If I were to design this game again, I would like to tidy up some code and make the whole codebase more modular as a whole. Also, I think I would implement this in a game engine like Ren'Py, which is set up for visual novels. I feel like adding more rpg elements would also be fun. Features like injuries and a moodle system (similar to PZ) would also make this a unique experience.

##### Citing Tools Used
Github CoPilot and CS50.ai were both utilized for debugging and as an aid in writing certain helper functions.
ChatGPT was used to help me design the format for this program, pointing out that splitting it into four python files can make it more modular.