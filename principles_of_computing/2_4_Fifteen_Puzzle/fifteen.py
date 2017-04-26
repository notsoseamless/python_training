"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors

jro - 10/08/2015

"""


#import poc_fifteen_gui



def manhattan_distance(row0, col0, row1, col1):
    """
    Compute the Manhattan distance between the cells
    (row0, col0) and (row1, col1)
    """
    return abs(row0 - row1) + abs(col0 - col1)
        




def move_target_in_col(clone, target_tile, direction, distance):
    ''' 
    helper moves target along a col
    '''
    target_tile_loc = clone.search_target_tile(target_tile)
    zero_tile_loc = clone.search_target_tile(0)
    move = ''
    if direction == 'u':
        pass
    elif direction == 'd':
        #print 'clone before', clone
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] < target_tile_loc[1]):
            # zero tile left of target
            move = 'dru' + ('lddru' * (distance - 1))
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] > target_tile_loc[1]):
            # zero tile right of target
            move = 'ullddru' + ('lddru' * (distance - 1))
        if (zero_tile_loc[0] < target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile above target
            move = 'lddru' * distance
        if (zero_tile_loc[0] > target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile below target
            move = 'u' + ('lddru' * (distance - 1))
        #print 'clone after', clone
    else:
        assert True, + 'Invalid col direction'
    clone.update_puzzle(move)
    return move


def move_zero_into_park(clone, target_row, target_col):
    '''
    helper puts zero cell in park
    '''
    move = ''
    zero_tile_loc = clone.search_target_tile(0)
    if zero_tile_loc != (target_row, (target_col - 1)):
        move = 'ld'
        clone.update_puzzle(move)            
    return move







def position_target_col0(clone, target_tile):
    '''
    Reposition the target tile to position (i-1,0)
    (i-1,0) = (target_row - 1, 0)

    Assume zero tile is adjacent to target tile
    '''
    total_moves = '' 
    move = ''
    target_col = 1
    target_tile_loc = clone.search_target_tile(target_tile)
    
    # target tile not in top row
    total_moves += move_target_from_top_row(clone, target_tile)
    
    # target in correct col
    if target_tile_loc[1] > (target_col):
        # move target left
        #print 'move target left by', (target_tile_loc[1] - (target_col))
        total_moves += move_target_in_row(clone, target_tile, 'l', (target_tile_loc[1] - target_col))
    elif (target_col) > target_tile_loc[1]:
        # move target right
        #print 'move target right by', (target_col - target_tile_loc[1])
        total_moves += move_target_in_row(clone, target_tile, 'r', (target_col - target_tile_loc[1]))            
    clone.update_puzzle(move)
    target_tile_loc = clone.search_target_tile(target_tile)

    # zero tile in correct row,col (0,j)
    zero_target_col = 0
    zero_target_row = target_tile_loc[1]
    zero_tile_loc = clone.search_target_tile(0)
    z_move = ''
    if zero_tile_loc[1] > zero_target_col:
        # move zero tile left
        if zero_tile_loc[0] == zero_target_row:
            # move over target tile
            z_move += 'u'
        z_move += 'l' * zero_tile_loc[1]
        clone.update_puzzle(z_move)
        total_moves += z_move
    zero_tile_loc = clone.search_target_tile(0)
    if zero_tile_loc[0] < zero_target_row:
        # move to top row
        z_move = 'd' * (zero_target_row - zero_tile_loc[0])
        clone.update_puzzle(z_move)
        total_moves += z_move
     
    return total_moves









def move_target_in_row(clone, target_tile, direction, distance):
    ''' 
    helper moves target along a row
    assume zero and target tiles are adjacent and target not in top row
    '''
    target_tile_loc = clone.search_target_tile(target_tile)
    zero_tile_loc = clone.search_target_tile(0)
    move = '' 
    print 'entering move_target_in_row\n', clone
    if direction == 'r':
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] < target_tile_loc[1]):
            # zero tile same row and left of target
            move = 'urrdl' * distance
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] > target_tile_loc[1]):
            # zero tile same row and right of target
            move = 'l' + ('urrdl' * (distance - 1))
        if (zero_tile_loc[0] < target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile above target
            #print 'distance', distance
            move = 'rdl' + ('urrdl' * (distance - 1))
        if (zero_tile_loc[0] > target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile below target
            move = 'rul' + ('urrdl' * (distance - 1))
    elif direction == 'l':
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] < target_tile_loc[1]):
            # zero tile same row and left of target
            move = 'r' + 'ulldr' * distance
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] > target_tile_loc[1]):
            # zero tile same row and right of target
            move = ('lrrdr' * (distance - 1))
        if (zero_tile_loc[0] < target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile above target
            move = 'ldr' + ('ulldr' * (distance ))
        if (zero_tile_loc[0] > target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile below target
            move = 'lur' + ('ulldl' * (distance - 1))
    else:
        assert True, + 'Invalid row direction'
    print 'clone before\n', clone
    print 'trying move:', move
    clone.update_puzzle(move)
    print 'clone after\n', clone
    return move
















def move_target_from_top_row(clone, target_tile):
    ''' 
    helper moves target down a row from top
    assume zero and target tiles are adjacent
    '''
    target_tile_loc = clone.search_target_tile(target_tile)
    zero_tile_loc = clone.search_target_tile(0)
    move = ''
    #print clone
    if target_tile_loc[0] == 0:
        # target in top row
        #print 'moving from top row'
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] < target_tile_loc[1]):
            # zero tile same row and left of target
            move = 'dru'
        elif (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] > target_tile_loc[1]):
            # zero tile same row and right of target
            move = 'dlu'
        elif (zero_tile_loc[0] > target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile same col and right of target
            move = 'u'
        else:
            assert True, + 'Invalid scenario'
        clone.update_puzzle(move)
        #print 'after move from top row\n', clone
    return move




def position_target_to_row(clone, target_tile, target_row):
    '''
    position target tile in row
    assumes zero tile is adjacent
    assume target not in top row
    '''
    move = ''       
    target_tile_loc = clone.search_target_tile(target_tile)
    zero_tile_loc = clone.search_target_tile(0)

    #print 'before row move\n', clone
    if target_tile_loc[0] != target_row:
        #print 'moving down by', (target_row - target_tile_loc[0])         
        if (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] < target_tile_loc[1]):
            # zero tile same row and left of target
            move = 'dru' + 'lddru' * ((target_row -1) - target_tile_loc[0])
        elif (zero_tile_loc[0] == target_tile_loc[0]) and (zero_tile_loc[1] > target_tile_loc[1]):
            # zero tile same row and right of target
            move = 'dlu' + 'lddru' * ((target_row -1) - target_tile_loc[0])
        elif (zero_tile_loc[0] > target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile same col and right of target
            move = 'u' + 'lddru' * ((target_row -1) - target_tile_loc[0])
        elif (zero_tile_loc[0] < target_tile_loc[0]) and (zero_tile_loc[1] == target_tile_loc[1]):
            # zero tile same col and above target
            if zero_tile_loc[1] == 0:
                # on left edge so move right first
                move = 'rddlu' * ((target_row) - target_tile_loc[0])                    
            else:
                move = 'lddru' * ((target_row) - target_tile_loc[0])                    
        else:
            assert True, + 'Invalid scenario'
        clone.update_puzzle(move)
    #print 'after row move\n', clone
    #print 'down move =', move
    return move



def dir_to_min_cell(clone, zero_tile, min_cell):
    '''
    helper translates neighbor to direction
    '''
    #print 'converting', zero_tile, min_cell
    if (zero_tile[0] == min_cell[0]) and (zero_tile[1] > min_cell[1]):
        return 'l'
    elif (zero_tile[0] == min_cell[0]) and (zero_tile[1] < min_cell[1]):
        return 'r'
    elif (zero_tile[0] > min_cell[0]) and (zero_tile[1] == min_cell[1]):
        return 'u'
    elif (zero_tile[0] < min_cell[0]) and (zero_tile[1] == min_cell[1]):
        return 'd'
    elif (zero_tile[0] == min_cell[0]) and (zero_tile[1] == min_cell[1]):         
        print clone, zero_tile, min_cell
        assert False, "invalid move: "
    else:         
        print clone, zero_tile, min_cell
        assert False, "invalid move: "






class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """
    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean             
        """     
        print 'called with', target_row, target_col
        # Tile zero is positioned at (target_row, target_col)
        if self.get_number(target_row, target_col) != 0:
            print 'lower_row_invariant failed for zero tile position'
            return False        
        # All tiles in rows i+1 or below are positioned at their solved location.
        # solved locations
        for row in range(target_row + 1, self.get_height()):
            for col in range(self.get_width()):
                if self.solved_value(row, col) != self.get_number(row, col):
                    return False        
        # All tiles in row i to the right of position (i,j) are positioned at their solved location.
        #print 'from', target_col + 1, self.get_width()
        for col in range((target_col + 1), self.get_width()):
            #print 'using range', range((target_col + 1))
            if self.solved_value(target_row, col) != self.get_number(target_row, col):
                return False          
        return True


    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """        

        total_moves = ''
        
        # clone the board
        clone = self.clone()

        # tile values
        target_tile = clone.solved_value(target_row, target_col)        
        target_tile_loc = clone.search_target_tile(target_tile)
        zero_tile_loc = clone.search_target_tile(0)

        # move zero tile to target tile
        print 'moving zero tile from', zero_tile_loc, 'to target tile', target_tile_loc
        total_moves += self._position_zero_tile(clone, target_tile_loc)       

        print 'after positioning zero on target\n', clone

        # now move target tile to target position
        target_tile_loc = clone.search_target_tile(target_tile)
        zero_tile_loc = clone.search_target_tile(0)
        if not (target_tile_loc == (target_row, target_col) and (zero_tile_loc ==  (target_row, (target_col - 1)))):
            # target tile not in top row
            total_moves += move_target_from_top_row(clone, target_tile)
            # target in correct col
            if (target_tile_loc[1] > target_col):
                print 'move target left by', (target_tile_loc[1] - target_col)
                total_moves += move_target_in_row(clone, target_tile, 'l', (target_tile_loc[1] - target_col))
            elif target_col > target_tile_loc[1]:
                # move target right
                total_moves += move_target_in_row(clone, target_tile, 'r', (target_col - target_tile_loc[1]))
        target_tile_loc = clone.search_target_tile(target_tile)
        zero_tile_loc = clone.search_target_tile(0)
        if not (target_tile_loc == (target_row, target_col) and (zero_tile_loc ==  (target_row, (target_col - 1)))):
            if target_row > target_tile_loc[0]:
                # move target down
                total_moves += move_target_in_col(clone, target_tile, 'd', (target_row - target_tile_loc[0]))

        # check zero tile in position
        total_moves += move_zero_into_park(clone, target_row, target_col)
        self.update_puzzle(total_moves)

        print 'final clone\n', clone

        return total_moves


    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0)
        
        # clone the board
        clone = self.clone()
        
        # get value of target tile
        target_tile = clone.solved_value(target_row, 0)

        total_moves = ''

        target_tile_loc = clone.search_target_tile(target_tile)
        zero_tile_loc = clone.search_target_tile(0)
        #print 'target_tile_loc', target_tile_loc
        #print 'target_row', target_row - 1
        if target_tile_loc == (target_row - 1, 0):
            # luck, move zero tile up one to position target_tile
            move = 'u'
            clone.update_puzzle(move)
            total_moves += move
        else:
            # manover target tile to suggested position
            #print 'positioning zero tile'
            target_tile_loc = clone.search_target_tile(target_tile)
            zero_tile_loc = clone.search_target_tile(0)
            total_moves += self._position_zero_tile(clone, target_tile_loc)
            #print clone
            
            # move from top row
            total_moves += move_target_from_top_row(clone, target_tile)

            # Reposition the target tile to position (i-1,1)
            # (i-1,1) = (target_row - 1, 1)
            total_moves += position_target_to_row(clone, target_tile, (target_row - 1))  
             
            #print 'after row move\n', clone
            
            total_moves += position_target_col0(clone, target_tile)
            
            #print 'after col move\n', clone

            # apply homework question 8 answer
            move = "ruldrdlurdluurddlur"
            clone.update_puzzle(move)
            total_moves += move

        #print clone
        # Finally, conclude by moving tile zero to the right end of row i-1.park zero tile
        # on right side       
        zero_tile_loc = clone.search_target_tile(0)
        distance = self._width - zero_tile_loc[1] - 1
        #print 'parking zero tile by', distance
        total_moves += 'r' * distance
        self.update_puzzle(total_moves)
        #print self
        assert self.lower_row_invariant(target_row - 1, self._width - 1)
        return total_moves


        
      

        
    def _position_zero_tile(self, clone, target_tile_loc):
        '''
        helper moves zero tile to target tile
        '''
        total_moves = ''
        while clone.search_target_tile(0) != target_tile_loc:
            zero_tile_loc = clone.search_target_tile(0)
            distance_field = self.create_distance_field([[target_tile_loc[0], target_tile_loc[1]], [target_tile_loc[0], target_tile_loc[1]]])
            #print 'df'
            neighbors = self.four_neighbors(zero_tile_loc[0], zero_tile_loc[1])
            #print 'neighbors', neighbors
            neighbors.sort()
            #print 'sorted neighbors', neighbors

            #print 'neighbors[1]', neighbors[1]
            min_cell = neighbors[0]
            #print 'min cell', min_cell
            min_distance = distance_field[min_cell[0]][min_cell[1]]
            #print 'min_distance', min_distance
            for neighbor in neighbors:
                #print 'surveying', neighbor[0], neighbor[1]
                #print 'neig value', clone.get_number(neighbor[0],neighbor[1])
                #print 'targ value', clone.get_number(neighbor[0],neighbor[1])
                if distance_field[neighbor[0]][neighbor[1]] < min_distance:
                    #print 'ddf', clone.get_number(neighbor[0],neighbor[1])
                    #if self.is_empty(neighbor[0],neighbor[1]):   
                    min_cell = (neighbor[0],neighbor[1])
                    min_distance = distance_field[neighbor[0]][neighbor[1]]
            #print 'min cell now', min_cell
            #print 'min_distance now', min_distance
            move = dir_to_min_cell(clone, zero_tile_loc, min_cell)
            #print 'clone before\n', clone
            clone.update_puzzle(move)
            #print 'move', move
            #print 'clone after\n', clone
            total_moves += move
        return total_moves



        


    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1):
        
        check tile zero is at (1,j) and whether all positions either below or 
        to the right of this position are solved
        
        Returns a boolean
        """
        # Tile zero is positioned in (target_col)
        if self.get_number(0, target_col) != 0:
            print 'row0_invariant: Failed col position value'
            return False        
        # All tiles in rows 2 or below are positioned at their solved location.
        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                if self.solved_value(row, col) != self.get_number(row, col):
                    print 'row0_invariant: Failed tiles in rows i+1'
                    return False 
        # All tiles in row i to the right of position (0,j) are positioned at their solved location.
        #print 'from', target_col + 1, self.get_width()
        #print 'range', range((target_col + 1), self.get_width())
        for col in range((target_col + 1), self.get_width()):
            #print 'check', self.solved_value(0, col), self.get_number(0, col)
            if self.solved_value(0, col) != self.get_number(0, col):
                print 'row0_invariant: Failed row i'
                return False 
        # Additionally check whether position (1,j) is also solved
        #print 'comparing',self.solved_value(1, target_col) , self.get_number(1, target_col)
        if self.solved_value(1, target_col) != self.get_number(1, target_col):
            print 'row0_invariant: Failed additional below test'
            return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # Tile zero is positioned at (target_col)
        if self.get_number(1, target_col) != 0:
            print 'row1_invariant: Failed position value', self.get_number(1, target_col)
            return False        
        # All tiles in rows i+1 or below are positioned at their solved location.
        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                if self.solved_value(row, col) != self.get_number(row, col):
                    print 'row1_invariant: Failed tiles in rows i+1'
                    return False        
        # All tiles in row i to the right of position (1,j) are positioned at their solved location.
        #print 'from', target_col + 1, self.get_width()
        #print 'range', range((target_col + 1), self.get_width())
        for col in range((target_col + 1), self.get_width()):
            #print 'check', self.solved_value(1, col), self.get_number(1, col)
            if self.solved_value(1, col) != self.get_number(1, col):
                print 'row1_invariant: Failed row 1'
                return False          
        return True
        
    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        
        # clone the board
        clone = self.clone()
        
        # get value of target tile
        target_tile = clone.solved_value(0, target_col)
        print 'target tile is', target_tile
        print clone
                
        total_moves = ''        
        target_tile_loc = clone.search_target_tile(target_tile)
        zero_tile_loc = clone.search_target_tile(0)
        if target_tile_loc[1] == target_col - 1 and target_tile_loc[0] == 0 and zero_tile_loc[1] == target_col:
            # only one move requireA
            move = 'ld'
            clone.update_puzzle(move)
            total_moves += move
            print 'after short move\n', clone

        elif target_tile_loc[1] != target_col:
            # moving target tile into (1, j-1)
            total_moves += self._position_zero_tile(clone, target_tile_loc)
            print 'after moving zero tile to target tile\n', clone
            
            target_tile_loc = clone.search_target_tile(target_tile)
            zero_tile_loc = clone.search_target_tile(0)
            # move target tile to suggested location
            suggested_loc = [1, target_col -1]
            if target_tile_loc != suggested_loc:
                # move target tile
                # target tile not in top row
                #print 'move from top row' 
                total_moves += move_target_from_top_row(clone, target_tile)
                #print 'clone after move from top\n', clone              
                # move to col
                target_tile_loc = clone.search_target_tile(target_tile)
                zero_tile_loc = clone.search_target_tile(0)
                if target_tile_loc[1] != suggested_loc[1]:
                    #print 'moving target right by', (suggested_loc[1] - target_tile_loc[1]) 
                    total_moves += move_target_in_row(clone, target_tile, 'r', (suggested_loc[1] - target_tile_loc[1]))
                    #print 'clone after moving right\n', clone
                # position zero tile at (1,j-2)
                #print 'positioning zero tile'
                zero_tile_loc = clone.search_target_tile(0)
                target_tile_loc = clone.search_target_tile(target_tile)
                suggested_zero_loc = (1, target_col -2)
                #print 'zero loc', zero_tile_loc, 'to',  suggested_zero_loc 
                if zero_tile_loc != suggested_zero_loc:
                    # move zero tile, assume  adjacent to target tile
                    #print 'need to move zero tile'
                    move = ''
                    if zero_tile_loc[1] == target_tile_loc[1]:
                        # above target tile
                        #print 'moving'
                        move = 'ld'
                    elif zero_tile_loc[1] == 0:
                        #print 'moving'
                        move = 'lld'
                    clone.update_puzzle(move)
                    total_moves += move
                    print 'clone after zero tile move\n', clone
                # now apply homework q10 move
                print 'apply q10 move'
                move = "urdlurrdluldrruld"
                clone.update_puzzle(move)
                total_moves += move
                #print 'clone after zero tile move\n', clone
                                                                   
        self.update_puzzle(total_moves)
        #print 'final layout\n', self
        return total_moves



    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        
        For rightmost n minus 2 columns of the remaining two rows, 
        one column at a time from right to left.
        
        Updates puzzle and returns a move string
        """
        #print 'solve_row1_tile called with', target_col
        
        # clone the board
        clone = self.clone()
        
        # get value of target tile
        target_tile = clone.solved_value(1, target_col)
                
        total_moves = ''
        
        # move zero tile to target tile
        #print clone
        target_tile_loc = clone.search_target_tile(target_tile)
        zero_tile_loc = clone.search_target_tile(0)
        total_moves += self._position_zero_tile(clone, target_tile_loc)
        #print clone
        
        # target tile not in top row
        total_moves += move_target_from_top_row(clone, target_tile)
        
        #print clone
       
        # target tile must be in row 1, move into correct col
        # target in correct col 
        target_tile_loc = clone.search_target_tile(target_tile)
        zero_tile_loc = clone.search_target_tile(0)
        #print 'target_tile_loc', target_tile_loc[1]
        #print 'target_col', target_col
        move = ''
        if target_tile_loc[1] > (target_col):
            # move target left
            #print 'move target left'
            move += move_target_in_row(clone, target_tile, 'l', (target_col - target_tile_loc[1]))
        elif (target_col) > target_tile_loc[1]:
            # move target right
            #print 'move target right by',  (target_col - target_tile_loc[1])
            move += move_target_in_row(clone, target_tile, 'r', (target_col - target_tile_loc[1]))

        #print clone
            
        # park zero tile above target tile
        zero_tile_loc = clone.search_target_tile(0)
        print 'zero at', zero_tile_loc
        if zero_tile_loc[0] != 0:
            #print 'moving zero'
            z_move = 'ur'
            clone.update_puzzle(z_move)
            move += z_move
            
        #print clone
                   
        total_moves += move
        self.update_puzzle(total_moves)
        #print 'returning', total_moves
        return total_moves


    

        

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
 
        # clone the board
        clone = self.clone()
        move = '' 
        num_10 = self._width
        num_11 = self._width + 1
        print 'solve_2x2 low nums', num_10, num_11
        if clone.get_number(0, 0) == 0 and clone.get_number(0, 1) == 1 and clone.get_number(1, 0) == num_10 and clone.get_number(1, 1) == num_11: 
            # nothing to do
            pass
        elif clone.get_number(0, 0) == 0 and clone.get_number(0, 1) == num_10 and clone.get_number(1, 0) == num_11 and clone.get_number(1, 1) == 1:
            # apply Q4
            move = 'rdlu'
        elif clone.get_number(0, 0) == 0 and clone.get_number(0, 1) == num_11 and clone.get_number(1, 0) == 1 and clone.get_number(1, 1) == num_10:
            # apply Q5
            move = 'rdlurdlu'
        elif clone.get_number(0, 0) == num_11 and clone.get_number(0, 1) == num_10 and clone.get_number(1, 0) == 1 and clone.get_number(1, 1) == 0:
            # owl test scenerio
            move = 'lurdlu'
        elif clone.get_number(0, 0) == num_11 and clone.get_number(0, 1) == num_10 and clone.get_number(1, 0) == 1 and clone.get_number(1, 1) == 0:
            # owl test scenerio
            move = 'ludruldrul'
        elif clone.get_number(0, 0) == num_10 and clone.get_number(0, 1) == 1 and clone.get_number(1, 0) == 0 and clone.get_number(1, 1) == num_11:
            # owl test scenerio
            move = 'u'
        elif clone.get_number(0, 0) == 1 and clone.get_number(0, 1) == num_10 and clone.get_number(1, 0) == num_11 and clone.get_number(1, 1) == 0:
            # owl test scenerio
            move = 'u'
        elif clone.get_number(0, 0) == num_10 and clone.get_number(0, 1) == 2 and clone.get_number(1, 0) == num_11 and clone.get_number(1, 1) == 1:
            # owl test scenerio
            move = 'ludruldrul'
        elif clone.get_number(0, 0) == num_10 and clone.get_number(0, 1) == 1 and clone.get_number(1, 0) == num_11 and clone.get_number(1, 1) == 0:
            # owl test scenerio
            move = 'lu'
        elif clone.get_number(0, 0) == num_10 and clone.get_number(0, 1) == 1 and clone.get_number(1, 0) == num_11 and clone.get_number(1, 1) == 0:
            # owl test scenerio
            move = 'lu'
        elif clone.get_number(0, 0) == 1 and clone.get_number(0, 1) == num_11 and clone.get_number(1, 0) == num_10 and clone.get_number(1, 1) == 0:
            # owl test scenerio
            move = 'ludruldruldruldrul'
        clone.update_puzzle(move)
        print clone

        self.update_puzzle(move)
        return move

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # clone the board
        clone = self.clone()
       
        total_moves = ''
        for row in range(self._height -1, 1, -1):
            for col in range(self._width -1, 0, -1):
                print 'processing', row, col 
                #assert self.lower_row_invariant(row, col)
                move = self.solve_interior_tile(row, col)
                total_moves += move
                clone.update_puzzle(move)
                print clone
            #assert self.lower_row_invariant(row, col)
            print 'calling solve_col0_tile() with', row
            move = self.solve_col0_tile(row)
            total_moves += move
            clone.update_puzzle(move)
            print clone
           

        for row in range(2):
            for col in range(self._width -1, 1, -1):
                print 'Now processing', row, col


                #assert my_puzzle.row1_invariant(self._width -1)
                print 'calling solve_row1_tile() with', col
                move = self.solve_row1_tile(col)
                total_moves += move
                clone.update_puzzle(move)
                print clone
                
                #assert my_puzzle.row0_invariant(self._width -1)
                print 'calling solve_row0_tile() with', col
                move = self.solve_row0_tile(col)
                #assert my_puzzle.row1_invariant(3 - 1)
                total_moves += move
                clone.update_puzzle(move)
                print clone

        move = self.solve_2x2()
        total_moves += move
        clone.update_puzzle(move)
        print clone
        
        #self.update_puzzle(total_moves)
        return total_moves

    ###########################################################
    # helpers
    
    def solved_value(self, row, col):
        '''
        helper returns solved value of a tile
        '''
        return col + (row * self.get_width())
    

    def search_target_tile(self, num):
        '''
        helper returns tile with value
        '''
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                if self.get_number(row, col) == num:
                    return(row, col)
        return(0,0)

    def create_distance_field(self, entity_list):
        """
        Create a Manhattan distance field that contains the minimum distance to 
        each entity (zombies or humans) in entity_list
        Each entity is represented as a grid position of the form (row, col) 
        """        
        distance_field = [[self._height + self._width \
                           for dummy_col in range(self._width)] \
                             for dummy_row in range(self._height)]
        for row in range(self._height):
            for col in range(self._width):
                distance = min([manhattan_distance(entity[0], entity[1], row, col) \
                            for entity in entity_list])
                distance_field[row][col] = distance
        return distance_field  


    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._width - 1:
            ans.append((row, col + 1))
        return ans    


    
# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(2, 2))


def simple_tests():
    '''
    some simple tests
    '''

    print
    print 'testing lower_row_invariant'
    print '==========================='
    print

    obj = Puzzle(2, 2, [[1, 2], [0, 3]])
    print True == obj.lower_row_invariant(1, 0)
    obj = Puzzle(2, 2, [[1,3], [0, 2]])
    print False == obj.lower_row_invariant(1, 0)   
    obj = Puzzle(4, 4, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print True == obj.lower_row_invariant(0, 0)   
    obj = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print True == obj.lower_row_invariant(0, 0)   
    obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
    print True == obj.lower_row_invariant(1, 1)       
    obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    print False == obj.lower_row_invariant(2, 0) 
    obj = Puzzle(4, 5, [[12, 11, 10, 9, 8], [7, 6, 5, 4, 3], [2, 1, 0, 13, 14], [15, 16, 17, 18, 19]])
    print True == obj.lower_row_invariant(2, 2)      
    obj = Puzzle(4, 4, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])               
    print True ==obj.lower_row_invariant(0, 0) 

    print '########################################'
    
    print
    print 'testing solve_interior_tile'
    print '==========================='
    print


    print '########################################'
    
    obj = Puzzle(2, 2, [[1, 2], [0, 3]])  
    print obj
    # todo assersion problem
    #print obj.solve_interior_tile(1, 0)
    print obj
    
    print '########################################'
    
    obj = Puzzle(2, 2, [[1, 2], [3, 0]])  
    print obj
    print obj.solve_interior_tile(1, 1)
    print obj
    
    print '########################################'
    
    obj = Puzzle(3, 3, [[1, 7, 6], [5, 4, 3], [8, 1, 0]])
    print obj
    move = obj.solve_interior_tile(2, 2)
    print obj
    
    print '########################################'
    
    obj = Puzzle(4, 4, initial_grid = [[13,  2,  3, 11],[4,  6,  7,  8],[9,  1, 10,  4],[15, 14, 12,  0]])   
    print obj
    move = obj.solve_interior_tile(3, 3)
    print obj
    
    print '########################################'
    
    obj = Puzzle(4, 4, initial_grid = [[15,  2,  3, 13],[4,  6,  7,  8],[9,  1, 10,  4],[11, 14, 12,  0]])   
    print obj
    move = obj.solve_interior_tile(3, 3)
    print obj

    print '########################################'
    
    
    obj = Puzzle(4, 4, initial_grid = [[13, 2, 3, 15],[4, 6, 7, 8],[9, 1,10, 4],[11, 14, 12,  0]])   
    print obj
    move = obj.solve_interior_tile(3, 3)
    print obj

    print '########################################'
    
    obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    print obj
    move = obj.solve_interior_tile(2, 2) 
    print obj


    print '########################################'
    
    obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    print obj
    move = obj.solve_interior_tile(2, 2)
    print move
    print obj

    print '########################################'
    
    print
    print 'testing solve_col0_tile'
    print '======================='
    print

    obj = Puzzle(3, 3, initial_grid = [[ 2,  3,  6],[ 5,  4,  1],[ 0,  7,  8]])                    
    print obj
    obj.solve_col0_tile(2)
    print obj

    print '=========================='
    
    obj = Puzzle(4, 5, [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]])
    print obj
    obj.solve_col0_tile(3) 
    print obj
    #returned incorrect move string (Exception: AssertionError) "move off grid: d" at line 288, in update_puzzle

    
    
    
    
    print
    print 'testing row1_invariant(j)'
    print '========================='
    print

    obj = Puzzle(4, 4, initial_grid = [[4, 6, 1, 3],[5, 2, 0, 7],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    print obj
    print obj.row1_invariant(2)

    print
    print 'testing row0_invariant(j)'
    print '========================='
    print

    obj = Puzzle(4, 4, initial_grid = [[6, 2, 0, 3],[5, 1, 4, 7],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    print obj
    print obj.row0_invariant(2)

    obj = Puzzle(4, 4, initial_grid = [[4, 2, 0, 3],[5, 1, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    print obj
    print obj.row0_invariant(2)

    print '======================================================================================='
    print
    print 'testing solve_row1_tile(j)'
    print '=========================='
    print

    obj = Puzzle(4, 4, initial_grid = [[4, 6, 1, 3],[5, 2, 0, 7],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    print obj
    obj.solve_row1_tile(2)
    print obj
    print obj.row1_invariant(2 - 1) 

    print '=========================='
    
    obj = Puzzle(4, 4, initial_grid = [[4, 7, 1, 3],[5, 2, 6, 0],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    print obj
    obj.solve_row1_tile(3)
    print obj
    print obj.row1_invariant(3 - 1) 

    print '=========================='
    
    obj = Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]])
    print obj
    obj.solve_row1_tile(2)
    print obj
    print obj.row1_invariant(2 - 1) 

    print '======================================================================================='

    print
    print 'testing solve_row0_tile(j)'
    print '=========================='
    print

    obj = Puzzle(4, 4, initial_grid = [[3, 6, 1, 0],[4, 5, 2, 7],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    #print obj
    #obj.solve_row0_tile(3)
    #print obj
    #print obj.row1_invariant(2 - 1) 

    print '=========================='

    #obj = Puzzle(4, 4, initial_grid = [[3, 6, 1, 0],[4, 5, 2, 7],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    #print obj
    #obj.solve_row0_tile(3)
    #print obj
    #print obj.row1_invariant(3 - 1) 

    #obj = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])
    #print obj
    #obj.solve_row0_tile(2)
    #print obj

    obj = Puzzle(4, 5, [[5, 2, 6, 3, 4], [1, 0, 7, 8, 9], [10, 11, 12, 13, 14], [15 , 16, 17, 18, 19]]) 
    print obj
    obj.solve_row0_tile(2)
    print obj
    #returned incorrect move string 'ldrurdlurdlurrdluldrruld'

    

    print '==================================================================================='

    print
    print 'testing solve_2x2(j)'
    print '===================='
    print

    #obj = Puzzle(4, 4, initial_grid = [[0, 4, 2, 3],[5, 1, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]])                    
    #print obj
    #obj.solve_2x2()
    #print obj


    #obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]])
    #print obj
    #obj.solve_2x2() 
    #print obj
    #returned incorrect move string ''


    #obj = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]]) 
    #obj = Puzzle(5, 4, [[5, 4, 2, 3], [1, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19]])
    #print obj
    #obj.solve_2x2()
    #print obj
    #returned incorrect move string ''




    print '=========================='



    print
    print 'testing solve_puzzle()'
    print '===================='
    print
    
    #obj = Puzzle(4, 4, initial_grid = [[12, 13, 14, 15], [4, 5, 2, 7],[8, 9, 10, 11],[3, 6, 1, 0]])                    
    #print obj
    #obj.solve_puzzle()
    #print obj

    #print obj
    #obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
    #print obj
    #obj.solve_puzzle()
    # returned incorrect move string (Exception: AssertionError) "move off grid: l" at line 107, in update_puzzle


    #obj = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
    #print obj
    #obj.solve_puzzle()
    #print obj
    #returned incorrect move string (Exception: AssertionError) "move off grid: l" at line 107, in 


    #print obj
    #obj = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
    #print obj
    #obj.solve_puzzle()
    #returned incorrect move string 

    obj = Puzzle(2, 4, [[0, 3, 2, 7], [4, 5, 6, 1]])

    print obj
    obj.solve_puzzle()
    print obj



simple_tests()








