"""
Clone of 2048 game.

02/06/2015

uses:
http://www.codeskulptor.org/#user40_AMu2IY1JvM_26.py


"""

import random
#import poc_2048_gui
#import user40_AMu2IY1JvM_30 as TestSuite2048
import  twenty_forty_eight_test as TestSuite2048


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # retain length of input for later
    original_line_length = len(line)

    def pack_line(line):
        '''
        Iterate over the line and return a list that has all the
        non-zero tiles slid over to the beginning of the list
        '''
        return [cell for cell in line if cell]
    
    # pack the line
    line = pack_line(line)
    # merge equal pairs (x2)
    for index in range(len(line)-1):
        if line[index] == line[index + 1]:
            # merge the two indexes
            line[index] *= 2
            # clear the old index
            line[index + 1] = 0

    # repack the line
    line = pack_line(line)
    # pad original list length with zeros
    line += ([0 for index in range(len(line), original_line_length)])
    return line



class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        ''' init method '''
        self._grid_height = grid_height # rows
        self._grid_width = grid_width # cols
        self._start_tiles = self.build_start_tiles()
        self._num_steps =  self.build_num_steps()
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # list of empty grid
        self._grid = [[0 for _ in range(self._grid_width)]  \
                       for _ in range(self._grid_height)]
        for _ in range(2):
            self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # As described in the "Grids" video, use the direction in the provided OFFSETS
        # dictionary to iterate over the entries of the associated row or column starting
        # at the specified initial tile. Retrieve the tile values from those entries, 
        # and store them in a temporary list.
        
        # Use your merge function to merge the tile values in this temporary list.
        
        # Iterate over the entries in the row or column again and store the merged tile
        # values back into the grid

        #self._offserts = self.build_offsets()
        #self._num_steps =  self.build_num_steps()

        def list_comp(list1, list2):
            '''
            compares two lists, if order has changed returns True
            '''
            #print 'comparing ' + str(list1) + '   ' + str(list2)
            for tile in range(len(list1)):
                if list1[tile] != list2[tile]:
                    return True
            return False

        tiles_changed = False
        for offset in range(len(self._start_tiles[direction])):
            old_line = self.get_row(self._start_tiles[direction][offset], OFFSETS[direction], self._num_steps[direction])
            new_line = merge(old_line)
            if list_comp(old_line, new_line):
                tiles_changed = True
                self.update_grid(self._start_tiles[direction][offset], OFFSETS[direction], self._num_steps[direction], new_line)
        # if any tiles changed then add a new tile
        if tiles_changed:
            self.new_tile()

        #print 'Updated  ' + str(direction) + '   ' + str(self._grid)

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # get list of the empty tiles
        empty_tiles = [[row,col] for col in range(self._grid_width) \
                       for row in range(self._grid_height) if self._grid[row][col] == 0]
        # chose a random tile from the empty_tiles
        random_tile = random.randint(0, len(empty_tiles)-1)
        # load it with a random 10%-90% choice
        self._grid[empty_tiles[random_tile][0]][empty_tiles[random_tile][1]] \
                                           = random.choice([2,2,2,2,2,2,2,2,2,4])

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        if ((col-1) <= self._grid_width) and ((row-1) <= self._grid_height): 
            self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        if ((col-1) <= self._grid_width) and ((row-1) <= self._grid_height): 
            return self._grid[row][col]        

    def build_start_tiles(self):
        '''
        compute a list of the indices for the initial tiles in that direction.
        Initial tiles are those whose values appear first in the list passed
        to the merge function.
        '''
        start_tiles = {}
        start_tiles[UP] = [(0, col)  for col in range(self._grid_width)]
        start_tiles[DOWN] = [( self._grid_height-1, col) for col in range(self._grid_width)]
        start_tiles[LEFT] = [( row, 0) for row in range(self._grid_height)]
        start_tiles[RIGHT] = [(row, self._grid_width-1) for row in range(self._grid_height)]
        return start_tiles
    
    def build_num_steps(self):
        ''' 
        calculates no of steps
        '''
        self._num_steps = {}
        self._num_steps[UP] = self._grid_height 
        self._num_steps[DOWN] = self._grid_height
        self._num_steps[LEFT] = self._grid_width
        self._num_steps[RIGHT] = self._grid_width
        return self._num_steps
        
    def get_row(self, start_cell, direction, num_steps):
        """
        Ripped from course material because it is a cool
        method that iterates through the cells in a grid
        in a linear direction
        """
        temp_line = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            temp_line.append(self._grid[row][col])
        return temp_line

    def update_grid(self, start_cell, direction, num_steps, new_data):
        '''
        Method adds new data to grid
        '''       
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self._grid[row][col] = new_data[step]



# run the test suit
TestSuite2048.run_suite(TwentyFortyEight)    
   
# run the gui
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

