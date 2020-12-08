#filename: parser.py

import gmap as mp

class Parser:
    def __init__(self):
        # A list of commands the parser recognizes. 
        self.recognized_commands = []
        # A list of nouns (and directions!) 
        self.recognized_nouns = []
        # Initialize a verb and noun both None
        self.verb, self.noun = None, None

    #a parser to separate verb and noun from user input
    def parse(self, phrase):
        phrase_as_list = phrase.split()
        # Check if first word of phrase is a recognized command verb
        parse_verb = phrase_as_list[0].lower()
        if parse_verb not in self.recognized_commands:
            print("Unrecognized verb:", parse_verb)
        else:
            self.verb = parse_verb
        # phrase is incomplete if length < 2 and phrase != exit    
        if len(phrase_as_list) < 2 and self.verb != 'exit':
            print("Please enter a complete phrase.")
        #extract noun from phrase, check against list
        if len(phrase_as_list) > 1:
            parse_noun = phrase_as_list[1].lower()
            if parse_noun not in self.recognized_nouns:
                print("Unrecognized noun:", parse_noun)
            else:
                self.noun = parse_noun
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
    # Define exit clause
    def continue_game(self):
        verb = self.get_verb()
        noun = self.get_noun()
        if verb == 'exit' and (noun == 'game' or noun is None):
            return False
        return True
    
    def go(self, current_tile):
        direction = self.get_noun()
        if direction not in ['up', 'down', 'north', 'east', 'south', 'west']:
            print("Invalid direction")
        else: 
            #get next tile by finding attribute with direction's name
            nxt_tile = getattr(current_tile, direction)
            # returns new current tile, see mp for travel documentation
            mp.game_map.travel(current_tile, nxt_tile)

    def use_item(self, item_name, obs_name):
        if item_name not in mp.ii.g_inv.items_by_name:
            print()

#game-specific parser
cmdp = GParser()
cmdp.recognized_commands = ['go', 'exit', 'view', 'take', 'use']
cmdp.recognized_nouns = ['north', 'east', 'south', 'west', 'up', 'down',
'game']
cmdp.recognized_nouns.extend(mp.ii.item_nouns)
print(cmdp.recognized_nouns)
