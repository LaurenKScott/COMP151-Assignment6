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
        
class Inventory:
    def __init__(self):
        # dictionary of items. key is item name, val is actual item object
        self.items_by_name = {}

    def in_inventory(self, item_name):
        if item_name in self.items_by_name:
            return True
        return False

    def add_item(self, item):
        #if item not already in inventory, add it
        if not self.in_inventory(item):
            self.items_by_name[item.get_name()] = item
            
        return self.items_by_name

    def rem_item(self, item_name):
        #if item is in inventory, remove it
        if self.in_inventory(item_name):
            del items_by_name[item_name]
        return self.items_by_name

    def describe_all(self):
        if self.items_by_name:
            for item in self.items_by_name.values():
                print(item.get_description())
        else:
            print("Your inventory is empty.")
        return self.items_by_name


    

#Initialize items in game, grouped by tile
all_items = Inventory()
#tile0
rock = Item('rock', 'a jagged black rock, perhaps flint')
all_items.add_item(rock)
#tile3
shovel = Item('shovel', 'a small shovel')
all_items.add_item(shovel)
grave = Obstacle('grave', 'thankfully, the grave is empty', None, shovel)
all_items.add_item(grave)
#tile6
axe = Item('axe', 'a rusted old axe, covered in barnacles')
all_items.add_item(axe)
boat = Obstacle('boat', 'the remains of a destroyed dinghy', None, axe)
all_items.add_item(boat)
#tile5
bread = Item('bread', 'some soggy old bread')
all_items.add_item(bread)
rations = Obstacle('crate', 'a wooden crate labelled "EMERGENCY RATIONS"',\
    shovel, bread)
all_items.add_item(rations)
#tile2
cotton = Item('cotton', 'scraps of cotton from an old sailor\'s coat')
all_items.add_item(cotton)
nest = Obstacle('nest', 'a strange looking nest of cotton scraps', None, cotton)
all_items.add_item(nest)
bird = Obstacle('seabird', 'a crippled old seagull with a knowing gaze',\
    bread, nest)
all_items.add_item(bird)
#tile4
key = Item('key', 'a large key on a silver chain')
all_items.add_item(key)
medusa = Obstacle('medusa', 'a fearsome creature', axe, key)
all_items.add_item(medusa)
mermaid = Obstacle('mermaid', 'a beautiful woman with the voice of an angel',\
    cotton, medusa)
all_items.add_item(mermaid)
#tile7
code = Item('code', 'a slip of paper that says: 9VK0A')
all_items.add_item(code)
book = Obstacle('book', 'a ragged book labelled "CAPTAIN\'S LOG"', None, code)
all_items.add_item(book)
shack = Obstacle('room', 'the dusty interior of a one-room shack', None, book)
all_items.add_item(shack)
door = Obstacle('door', 'a locked door', key, shack) 
all_items.add_item(door)
#tile8
oil = Item('oil', 'a full canister of oil')
all_items.add_item(oil)
#tile10
unlit_wick = Obstacle('wick', 'the wick needs a spark to ignite', rock, "win")
all_items.add_item(unlit_wick)
empty_tank = Obstacle('tank', 'the fuel tank is empty', oil, unlit_wick)
all_items.add_item(empty_tank)

#tile9
hatch = Obstacle('hatch', 'a keypad to unlock the hatch', code, empty_tank)
all_items.add_item(hatch)

#Initialize player inventory that is empty
player_inv = Inventory()
