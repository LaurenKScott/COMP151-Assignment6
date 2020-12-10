#filename: parser.py

import gmap as mp

class Parser:
    def __init__(self):
        # A list of commands the parser recognizes. 
        self.recognized_commands = []
        # A list of nouns (and directions!) 
        self.recognized_nouns = []
        self.verb, self.noun = None, None

    #Check input phrase for validity
    def valid(self, phrase):
        if phrase.strip() == '':
            print("No command given")
            return False
        # break phrase into list of words
        phrase_as_list = phrase.split()
        # check first word (lowercase) against recognized commands
        check_verb = phrase_as_list[0].lower()
        if check_verb not in self.recognized_commands:
            print("Unrecognized command:", check_verb)
            return False
        #only 'view' and 'exit' are valid one-word command phrases
        if len(phrase_as_list) < 2 and not \
            (check_verb =='exit' or check_verb =='view'):
            print("Incomplete phrase.")
            return False
        # if phrase is 2 words or greater
        elif len(phrase_as_list) > 1:
            # consider 2nd word as noun. check against recognized nouns
            check_noun = phrase_as_list[1].lower()
            if check_noun not in self.recognized_nouns:
                print("Unrecognized noun:", check_noun)
                return False
        # if noun and verb both recognized
        return True

    #a parser to separate verb and noun from user input
    def parse(self, phrase):
        self.verb, self.noun = None, None
        while not self.valid(phrase):
            phrase = input("Try again." )
        else:
            verb_noun = phrase.split()
            self.verb = verb_noun[0].lower()
            if len(verb_noun) > 1:
                self.noun = verb_noun[1].lower()
        #returns verb, noun tuple
        return self.verb, self.noun
    
    # Getter method for verb
    def get_verb(self):
        return self.verb

    # Getter method for noun
    def get_noun(self):
        return self.noun

class GParser(Parser):
    def __init__(self):
        Parser.__init__(self)

    def cannot_do(self):
        print("Can't do that.", end=" ")

    # Define exit clause
    def continue_game(self):
        verb = self.get_verb()
        noun = self.get_noun()
        if verb == 'exit' and (noun == 'game' or noun is None):
            return False
        return True
    
    def go(self, direction):
        current_tile = mp.game_map.get_location()
        if direction not in ['up', 'down', 'north', 'east', 'south', 'west']:
            print("Invalid direction")
        else: 
            #get next tile by finding attribute with direction's name
            nxt_tile = getattr(current_tile, direction)
            # returns new current tile, see mp for travel documentation
            mp.game_map.travel(nxt_tile)

    def view(self, inp_noun):
        #view inventory condition
        if inp_noun == "inventory":
            mp.ii.player_inv.describe_all()
        # if no noun is given (i.e. 'view '),
        elif inp_noun == None:
        # view current tile description
            current_tile = mp.game_map.get_location()
            print(current_tile.get_description())
        # if input noun is in current tile
        else:
            tile_inv =  mp.game_map.get_location().inv
            if tile_inv.in_inventory(inp_noun):
                print(tile_inv.items_by_name[inp_noun].get_description())
            else:
                self.cannot_do()
        return None

    #take item works only on items not obstacles, thus don't worry
    #about setting tile item to None
    def take_item(self, item):
        #if item present in current location
        if mp.game_map.get_location().has_item(item.get_name()):
            mp.ii.player_inv.add_item(item)
            print(item.get_name(), "added to inventory.")
            mp.game_map.get_location().item = None
        else:
            self.cannot_do()
            print("Item not found:", item.get_name())

    def use_item(self, item_name):
        current_location = mp.game_map.get_location()
        # IF the item in the location is an instance of Obstacle,
        if isinstance(current_location.item, mp.ii.Obstacle):
            # AND the item name matches the name of the obstacle's weakness,
            if item_name == current_location.item.weakness.get_name():
                # THEN find item in inventory's items by name dict
                item_used = mp.ii.player_inv.items_by_name[item_name]
                # call rem_item method on player_inv, (return updated inv)
                mp.ii.player_inv.rem_item(item_used)
                #set new obstacle (or item) to unlocked 
                current_location.item = current_location.item.unlock
                # adjust tile's inventory
                current_location.build_inv()
            # if attempting to use an item not in player's inventory
            elif item_name not in mp.ii.player_inv.items_by_name:
                self.cannot_do()
                print(item_name, "not in inventory.")
        # if the item in room is not an obstacle, or there is no item
        else:
            self.cannot_do()
            print(item_name, "didn't work.")

    def command_choose(self):
        if self.get_verb() == 'view':
            self.view(self.get_noun())
        elif self.get_verb() == 'go':
            self.go(self.get_noun())
        elif self.get_verb() == 'take':
            item = mp.ii.all_items.items_by_name[self.get_noun()]
            self.take_item(item)
        elif self.get_verb() == 'use':
            self.use_item(item=self.get_noun())

#game-specific parser
cmdp = GParser()
cmdp.recognized_commands = ['go', 'exit', 'view', 'take', 'use']
cmdp.recognized_nouns = ['north', 'east', 'south', 'west', 'up', 'down',
'game']
cmdp.recognized_nouns.extend(mp.ii.all_items.items_by_name.keys())
