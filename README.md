# The Lighthouse
***A text-based adventure in Python***

<p>Premise: you awake after a storm on a tiny island. Looking around, you find an abandoned lighthouse, as well as some unsettling clues about the last lightkeeper's fate. With only your wits and the objects you find, can you reach the lighthouse and signal for help?</p>

Inspired by Robert Eggers' film *The Lighthouse* (2019) 

## How to Play
<p> clone repo and run adventure.py </p>
<p> when prompted, enter a command. 'commands' are one or two-word phrases consisting of a verb and (optionally) a noun or direction. </p>
<br>
*stuck? start with 'view' to see a description of your current location!*

### Files
iteminventory.py: contains the Item, Obstacle, and Inventory classes 

gmap.py: contains the Tile and Grid class, which utilize linked list concepts to help the player navigate a 3-D map   

gameparse.py: the Parser class, which takes player inputs and translates them to commands in the game   

adventure.py: this is where the game itself is played  

Island_Map.svg: scalable diagram showing tile-to-tile relationships

### Walkthrough [Spoilers!]
> take rock <br>
> go up. go west. go north <br>
> view grave. take shovel <br>
> go east <br>
> use shovel. take bread <br>
> go north <br>
> view boat. take axe <br>
> go south. go south. go west <br>
> use bread. view nest. take cotton <br>
> go north. go north <br>
> use cotton. use axe. take key. <br>
> go south. go south. go east. go east <br>
> use key. view book. take code. <br>
> go north <br> 
> take oil <br>
> go up. go up <br>
> use code. use oil. use rock. (win)