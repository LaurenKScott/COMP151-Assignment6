# The Lighthouse
***A text-based adventure in Python***

<p>Premise: you awake after a storm on a tiny island. Looking around, you find an abandoned lighthouse, as well as some unsettling clues about the last lightkeeper's fate. With only your wits and the objects you find, can you reach the lighthouse and signal for help?</P>

<p> Inspired by Robert Eggers' film *The Lighthouse* (2019)

### Files
iteminventory.py: contains the Item, Obstacle, and Inventory classes 

gmap.py: contains the Tile and Grid class, which utilize linked list concepts to help the player navigate a 3-D map   

gameparse.py: the Parser class, which takes player inputs and translates them to commands in the game   

adventure.py: this is where the game itself is played  

Island_Map.svg: scalable diagram showing tile-to-tile relationships

### Walkthrough [Spoilers!]
> take rock <br>
> go up <br>
> go west <br>
> go north <br>
> view grave. take shovel. <br>
> go east <br>
> use shovel. take bread. <br>
> go north <br>
> view boat. take axe. <br>
> go south <br>
> go south <br>
> go west <br>
> use bread. view nest. take cotton. <br>
> go north <br>
> go north <br>
> use cotton. use axe. take key. <br>
> go south <br>
> go south <br>
> go east <br>
> go east <br>
> use key. view book. take code. <br>
> go north <br> 
> take oil <br>
> go up <br>
> go up <br>
> use code. use oil. use rock. (win)