"""

"""
#import iteminventory module to place items in tiles
import iteminventory as ii

class Tile:
    def __init__(self, des, item=None, obs=None,
     nor=None, eas=None, sou=None, wes=None, up=None, dwn=None):
        self.description = des
        self.item = item
        self.obs = obs
        self.north = nor
        self.east = eas
        self.south = sou
        self.west = wes
        self.up = up
        self.down = dwn
    
    def get_description(self):
        return self.description
    
    def has_item(self, item_name):
        if item_name == self.item.get_name():
            return True
        return False

class Grid:
    def __init__(self, start_pos = None):
        self.start_pos = start_pos

    def travel(self, current, nxt):
        if nxt is None:
            print("Can't go there")
        else:
            current = nxt
        return current

# initialize nodes with descriptions 
tile0 = Tile('You are on a rocky beach. ')
tile1 = Tile('nothing here you are on an island')
tile2 = Tile('old seabird looks at you')
tile3 = Tile('what appears to be a shallow grave')
tile4 = Tile('mermaid cove')
tile5 = Tile('behind the lighthouse, a half-buried crate')
tile6 = Tile('dock with smashed boat')
tile7 = Tile('a locked door to shack')
tile8 = Tile('ground floor lighthouse')
tile9 = Tile('up the stairs, hatch')
tile10 = Tile('top floor empty tank')

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
tile2.obs = ii.bird #use bread to unlock nest, unlocks cotton
tile3.obs = ii.grave #unlocks shovel
tile4.obs = ii.mermaid #unlocks medusa, then use axe to unlock key
tile5.obs = ii.rations #use shovel to unlock bread
tile6.obs = ii.boat #unlocks axe

#initialize game map
game_map = Grid(start_pos=tile0)
