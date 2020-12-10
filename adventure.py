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
current_loc= mp.game_map.start_pos
#Initialize parser
parser = pr.cmdp

def win_condition():
    if ii.unlit_wick.unlock == True:
        print("you win")
        return True
    return False
#set win condition
def main():
    print("Welcome to The Lighthouse.")
    while parser.continue_game():
        print(current_loc.get_description())
        user_command = input("Enter a command: ")
        parser.parse(user_command)
        parser.command_choose()
    else:
        print("Goodbye.")
        exit
main()
