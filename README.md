# The Lighthouse
***A text-based adventure in Python***

<p>Premise: you awake after a storm on a tiny island. Looking around, you find an abandoned lighthouse, as well as some unsettling clues about the last lightkeeper's fate. With only your wits and the objects you find, can you reach the lighthouse and signal for help?</P>

### Files
iteminventory.py: contains the Item, Obstacle, and Inventory classes 

gmap.py: contains the Tile and Grid class, which utilize linked list concepts to help the player navigate a 3-D map   

gameparse.py: the Parser class, which takes player inputs and translates them to commands in the game   

adventure.py: this is where the game itself is played  


### Walkthrough [Spoilers!]
> take rock
> go up 
> go west
> go north
> view grave. take shovel.
> go east
> use shovel. take bread.
> go north
> view boat. take axe.
> go south
> go south
> go west
> use bread. view nest. take cotton.
> go north
> go north
> use cotton. use axe. take key.
> go south
> go south
> go east
> go east
> use key. view book. take code.
> go north
> take oil
> go up
> go up
> use code. use oil. use rock. ("win")