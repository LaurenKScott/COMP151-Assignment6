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
inv = ii.g_inv
#initialize island map (see map.py for tile info)
island = mp.game_map

#Initialize parser
parser = pr.cmdp

#set win condition
def main():
    print("Welcome to The Lighthouse.")
    while parser.continue_game():
        user_command = input("Enter a command: ")
    else:
        print("Goodbye.")
        exit
main()
