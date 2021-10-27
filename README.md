# Unit 1: A classic game 
![](game.gif)

# Criteria A: Planning

## Problem definition

The owner of the local game shop is an enthusiast of classic computer games. He has been looking for a talented programmer that can help him revive his passion for text-based games. He has few requirements for this task:

1. The game has to be entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score.

Apart for these requirements, the owner is open to any type of game, topic or genre.

## Proposed Solution

I am going to create a Pokemon based text game, this will allow you to play against a friend on the same PC or against a CPU using the 3 base pokemon types of fire, water, and grass. The game will be produced using Python Version 3.9, and will run through a python console.

## Success Criteria
1. The game has to be entirely text-based.
2. The game must record the time played.
3. The game must record the player name and score.
4. Have the option of the three basic elements: fire, water, and grass, along with unique movesets for each element
5. Option for PvP or PvCPU
6. Database integration for numerous save states

# Criteria B: Design

## System Diagram

![](System_Diagram.png)

**Figure 1.** System Diagram for proposed text game

As shown in **Fig. 1**, the solution will run on python and is developed using the Eclipse IDE. The code it designed on windows but can run on mac or linux os systems using a python 3.9 console.

## UML Diagram

**Figure 2.** UML Diagram for the player class
![](playerUML.png)

As shown in **Figure 2**, this is a UML diagram depicting my class 'player' that is used, along with the attributes associated with the class used. The class has no functions directly connected to it, but does use a few attributes, specifically it uses: Name, the name of the player, element, the element used by the player, hp, which is the amount of health left, acc_amt, which is the amount of times you can use each attack, weakness, element to which the player object is weak to, strong, which is the element to which the player is strong to, and moves, which is a list containing all possible moves based off of our element attribute.

## Flow Diagrams
**Figure 3**
Fig. 3 is a CPU Turn Function Flow Diagram, this depicts the method through which the CPU decided which move to use, based off of what element the CPU attribute is. This is done through a random number generator, then an if statement checks which element the CPU is attributed to, after which is uses the corresponding move based off the random number generated.

![](export_canvas_cpu-command-selection-210922_2204.png)


**Figure 4**
Fig 4 is a portion of code that sets up the game, namely by creating player objects based off the user inputs and game type. It starts off by asking for player 1s name, and whether or not they will dod PvP which is to play with the person next to you, or PvCPU. It then asks for the pokemon type player 1 wants, after which it creates a object from the player class, using the name and element entered above. This is repeated for player 2 if the game type is PvP, or if the game type is PvCPU it uses a random number to assign a element to the CPU, which is another instance of the player class.

![](setupchart.png)

**Figure 5**
Fig 5 is the function that itterates a battle until either side has lost. This is done with a while loop, only breaking out of the loop once either player reaches 0 HP 

![](BattleDiagram.png)

##Setup Input Unit Testing


## Record of Tasks
| Task No | Planned Action | Planned Outcome | Time estimate | Target completion date | Criterion |
|---|---|---|---|---|---|
| 1 | Work on CPU Action | Fix formatting, start theorizing how to calculate CPU actions | 2 Hours | September 19th | C |
| 2 | Finish CPU Implementation, consider something else? | Decided on inclusion of music or ascii images, finish CPU if else ladder | 2 Hours | September 20th | C |
| 3 | Comments and playtesting | Fill out comment descriptions for every function and if statements that are not clear | 1.5 Hours | September 21st | C |
| 4 | write out first system diagram, start second flowchart | Upload first system diagram | 30 mins | September 24th | B |
| 5 | Debug and test, try the game with every possible unique input,  to confirm everything is fully operational | Make a log of all detected bugs or errors | 1 Hour | September 30th | C |
| 6 | Caesar Cypher encoder written out | Success | 30 mins | October 5th | C |
| 7 | Database caesar cypher implementation | Database is in Caesar cypher, TODO// get database to work  | 20 mins | October 5th | C |
| 8 | Battle function flow chart | Completed | 10 mins | October 7th | B |
| 9 | Fixed Battle Function chart | Fixed Loop | 10 Mins | October 22nd | B |
| 10 | Make flowchart diagram for game setup | Finish flowchart and add to repo | 30mins | October 23rd | B |
| 11 | Proofread and explain flow diagrams in more detail | Finish all flowchart descriptions | 1 Hour | October 26th | B |
