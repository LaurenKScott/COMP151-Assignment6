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
player_inv = ii.player_inv
#initialize island map (see map.py for tile info)
island = mp.game_map
#Initialize parser
parser = pr.cmdp

def win_condition():
    if island.get_location() == mp.tile10 and island.get_location().item is None:
        print("you win")
        return True
    return False
#set win condition
def main():
    print("Welcome to The Lighthouse.")
    print()
    print(island.get_location().get_description())

    while parser.continue_game() and not win_condition():
        user_command = input("Enter a command: ")
        parser.parse(user_command)
        parser.command_choose()
    else:
        print("Goodbye.")
        exit
main()
