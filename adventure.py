# File: adventure.py
# A simple text adventure game

"""

HOW TO PLAY
Objective - get to the top of the lighthouse and signal for help.
Instructions - when prompted, enter a command into the terminal. commands are one or two word phrases
consisting of a verb and a noun or direction. use commands to move around the map and to interact with objects 

"""

# import modules
import iteminventory as ii
import gmap as mp
import gameparse as pr 

#Initialize player's empty inventory (see iteminventory.py)
player_inv = ii.player_inv
#initialize island map (see map.py for tile info)
island = mp.game_map
#Initialize parser (see gameparse.py for command info)
parser = pr.cmdp

#set win condition
def win_condition():
    if island.get_location() == mp.tile10 and island.get_location().item is None:
        print("you win")
        return True
    return False

# gameplay function, takes string user_command and parses input. then translates into executable command
def play_game():
    user_command = input("Enter a command: ")
    parser.parse(user_command)
    print()
    parser.command_choose()
    print()
   

def main():
    # start of game, print initial tile description
    print("THE LIGHTHOUSE")
    print()
    print(island.get_location().get_description())
    while parser.continue_game() and not win_condition():
        play_game()
    else:
        print("Goodbye.")
        
if __name__ == '__main__':
    main()
