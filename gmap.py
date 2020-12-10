
#import iteminventory module to place items in tiles
import iteminventory as ii

class Tile:
    def __init__(self, des, item=None, inv=None,
     nor=None, eas=None, sou=None, wes=None, up=None, dwn=None):
        self.description = des
        self.item = item
        self.inv = ii.Inventory()
        self.north = nor
        self.east = eas
        self.south = sou
        self.west = wes
        self.up = up
        self.down = dwn
    
    def get_description(self):
        if self.item is not None:
            return self.description + "There is " + self.item.get_description()
        return self.description

    def build_inv(self):
        if self.item is not None:
            self.inv.add_item(self.item)

    def has_item(self, item_name):
        if item_name in self.inv.items_by_name:
            return True
        return False

class Grid:
    def __init__(self, start_pos = None, current_pos=None):
        self.start_pos = start_pos
        self.current_pos = current_pos
    
    def get_location(self):
        #returns a tile
        return self.current_pos

    def travel(self, nxt):
        if nxt is None:
            print("Can't go there")
        else:
            self.current_pos = nxt
        return self.current_pos

# initialize nodes with descriptions 
tile0 = Tile('You are on a rocky beach. ')
tile1 = Tile('nothing here you are on an island ')
tile2 = Tile('old seabird looks at you ')
tile3 = Tile('what appears to be a shallow grave' )
tile4 = Tile('mermaid cove' )
tile5 = Tile('behind the lighthouse, a half-buried crate ')
tile6 = Tile('dock with smashed boat ')
tile7 = Tile('a locked door to shack ')
tile8 = Tile('ground floor lighthouse ')
tile9 = Tile('up the stairs, hatch ')
tile10 = Tile('top floor empty tank ')

# set up tile links on map (relative directions see map)
tile0.up = tile1
tile1.down, tile1.north, tile1.west, tile1.east = tile0, tile5, tile2, tile7
tile2.north, tile2.east = tile3, tile1
tile3.north, tile3.south, tile3.east = tile4, tile2, tile5
tile4.south = tile3
tile5.north, tile5.south, tile5.west = tile6, tile1, tile3
tile6.south = tile5
tile7.west, tile7.north = tile1, tile8
tile8.south, tile8.up = tile7, tile9
tile9.down, tile9.up = tile8, tile10
tile10.down = tile9

#place obstacles in proper tiles (see iteminventory.py)

tile0.item = ii.rock
tile0.build_inv()

tile1.build_inv()

tile2.item = ii.bird
tile2.build_inv()

tile3.item = ii.grave
tile3.build_inv()

tile4.item = ii.mermaid
tile4.build_inv()

tile5.item = ii.rations
tile5.build_inv()

tile6.item = ii.boat
tile6.build_inv()

tile7.item = ii.door
tile7.build_inv()

tile8.item = ii.oil
tile8.build_inv()

tile9.item = ii.hatch
tile9.build_inv()

tile10.item = ii.empty_tank
tile10.build_inv()

#initialize game map
game_map = Grid(start_pos=tile0, current_pos=tile0)

