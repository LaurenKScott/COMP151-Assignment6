"""
Filename: iteminventory.py
Description: Defines an item and inventory class to be used in adventure game
(see README.md of project directory)
Author: Lauren K. Scott
"""

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    # getter method to return item's name
    def get_name(self):
        return self.name
    
    # getter method to safely retrieve item description
    def get_description(self):
        return self.description
    
    
class Obstacle(Item):
    def __init__(self, name, description, weakness, unlock):
        Item.__init__(self, name, description)
        #defines the item that will defeat obstacle
        self.weakness = weakness
        #the item or next obstacle that is revealed upon defeat
        self.unlock = unlock

    def defeat(self, input_obj):
        if self.weakness is None:
            return True
        elif input_obj.get_name() == self.weakness.get_name():
            return True
        return False
class Inventory:
    def __init__(self):
        # dictionary of items. key is item name, val is actual item object
        self.items_by_name = {}

    def in_inventory(self, item):
        i_name = item.get_name()
        if i_name in self.items_by_name:
            return True
        return False

    def add_item(self, item):
        #if item not already in inventory, add it
        if not self.in_inventory(item):
            self.items_by_name[item.get_name()] = item
            print(item.get_name(), "added to inventory.")
        return self.items_by_name

    def rem_item(self, item):
        #if item is in inventory, remove it
        if self.in_inventory(item):
            del items_by_name[item.get_name()]
        return self.items_by_name

    def describe_all(self):
        if self.items_by_name():
            for item in self.items_by_name.values():
                print(item.get_description())
        else:
            print("Your inventory is empty.")
        return None

    

#Initialize items in game, grouped by tile
#tile0
rock = Item('rock', 'a jagged black rock, perhaps flint')
#tile3
shovel = Item('shovel', 'a small shovel')
grave = Obstacle('grave', 'thankfully, the grave is empty', None, shovel)
#tile6
axe = Item('axe', 'a rusted old axe, covered in barnacles')
boat = Obstacle('boat', 'the remains of a destroyed dinghy', None, axe)
#tile5
bread = Item('bread', 'some soggy old bread')
rations = Obstacle('crate', 'a wooden crate labelled "EMERGENCY RATIONS"',\
    shovel, bread)
#tile2
cotton = Item('cotton', 'scraps of cotton from an old sailor\'s coat')
nest = Obstacle('nest', 'a strange looking nest of cotton scraps', None, cotton)
bird = Obstacle('seabird', 'a crippled old seagull with a knowing gaze',\
    bread, nest)
#tile4
key = Item('key', 'a large key on a silver chain')
medusa = Obstacle('medusa', 'a fearsome creature', axe, key)
mermaid = Obstacle('mermaid', 'a beautiful woman with the voice of an angel',\
    cotton, medusa)

#tile7
code = Item('code', 'a slip of paper that says: 9VK0A')
book = Obstacle('book', 'a ragged book labelled "CAPTAIN\'S LOG"', None, code)
shack = Obstacle('room', 'the dusty interior of a one-room shack', None, book)
door = Obstacle('door', 'a locked door', key, shack) 
#tile8
oil = Item('oil', 'a full canister of oil')

#tile10
unlit_wick = Obstacle('wick', 'the wick needs a spark to ignite', rock, None)
empty_tank = Obstacle('tank', 'the fuel tank is empty', oil, unlit_wick)

#tile9
hatch = Obstacle('hatch', 'a keypad to unlock the hatch', code, empty_tank)

#list of all item names to be recognized by a parser
item_nouns = [rock.get_name(), shovel.get_name(), grave.get_name(),
axe.get_name(), boat.get_name(), bread.get_name(), cotton.get_name(), 
nest.get_name(), key.get_name(), code.get_name(), book.get_name(), 
shack.get_name(), oil.get_name()]

#GAME INVENTORY
g_inv = Inventory()