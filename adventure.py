# File: adventure.py
# A simple text adventure game

"""

RULES AND OBJECTIVES: TBD

"""

# import modules
import iteminventory as ii
import gmap as mp
import gameparse as pr 

#Initialize inventory
inv = ii.Inventory()
#initialize island map (see map.py for tile info)
island = mp.game_map

#Initialize parser
parser = pr.cmdp

#set win condition
def main():
    print(inv)

main()
