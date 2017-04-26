"""
Student portion of Zombie Apocalypse mini-project

JRO - 19/07/2015

"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7
  

class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []            
            
    def __str__(self):
        """
        Return human readable string.
        """
        human_str = 'Humans: ' + str(self._human_list)
        zombie_str = 'Zombies: ' + str(self._zombie_list)
        return 'Grid:\n' + poc_grid.Grid.__str__(self) + human_str + '\n' + zombie_str + '\n'
         
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []        
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)        
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # empty grid "visited" of the same size as the original grid
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        
        # 2D list distance_field of the same size as the original grid
        entry_val = self._grid_height * self._grid_width # init with max poss val
        distance_field = [[entry_val for _ in range(self._grid_width)] for _ in range(self._grid_height)]   
        print 'distance_field', distance_field
                
        # Create a queue "boundary" that is a copy of either the zombie list or the human list. 
        boundary = poc_queue.Queue()        
        def copy_queue(sub_list):
            """
            helper to copy list into queue
            """
            for sub in sub_list:
                boundary.enqueue(sub)        
               
        if entity_type == HUMAN:
            copy_queue(self._human_list)
        else:
            copy_queue(self._zombie_list)

        # For cells in the queue, initialize visited to be FULL and distance_field to be zero.
        for cell in boundary.__iter__():
            print 'init', cell[0], cell[1]
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0
            
        # Finally, implement a modified version of the BFS search. 
        # For each neighbor_cell in the inner loop, check whether the cell has not been visited 
        # and is passable. If so, update the visited grid and the boundary queue as specified. 
        # In this case, also update the neighbor's distance to be the distance to current_cell
        while len(boundary) > 0:
            for cell in boundary.__iter__():
                cell = boundary.dequeue()
                neighbors = visited.four_neighbors(cell[0], cell[1])
                for neighbor in neighbors:
                    if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]): 
                        print 'inner', neighbor[0], neighbor[1]
                        visited.set_full(neighbor[0], neighbor[1])
                        boundary.enqueue(neighbor)
                        distance_field[neighbor[0]][neighbor[1]] = (distance_field[cell[0]][cell[1]] + 1)  
        # update blocked cells
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                if not self.is_empty(row,col):
                    distance_field[row][col] = entry_val
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        # create temp copy of human list
        temp_humans = list(self._human_list)
        for human in temp_humans:
            # get neibour cell distances to zombieseight_neighbors
            neighbors = self.eight_neighbors(human[0], human[1])
            #self.print_df(zombie_distance_field)
            #print self.eight_neighbors(human[0], human[1])
            max_cell = (human[0], human[1])
            max_distance = zombie_distance_field[human[0]][human[1]]
            for neighbor in neighbors:
                if zombie_distance_field[neighbor[0]][neighbor[1]] > max_distance:
                    if self.is_empty(neighbor[0],neighbor[1]):   
                        max_cell = (neighbor[0],neighbor[1])
                        max_distance = zombie_distance_field[neighbor[0]][neighbor[1]]
            #print 'human', human
            self._human_list.remove(human)
            self._human_list.append(max_cell)         

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        # create temp copy of zombie list
        temp_zombies = list(self._zombie_list)
        for zombie in temp_zombies:
            # get neibour cell distances to zombieseight_neighbors
            neighbors = self.four_neighbors(zombie[0], zombie[1])
            #self.print_df(human_distance_field)
            #print self.four_neighbors(zombie[0], zombie[1])
            min_distance = human_distance_field[zombie[0]][zombie[1]]
            min_cell = (zombie[0], zombie[1])
            #print 'min cell', min_cell, human_distance_field[zombie[0]][zombie[1]]
            for neighbor in neighbors:
                #print 'neighbors', neighbor
                if human_distance_field[neighbor[0]][neighbor[1]] < min_distance:
                    #if self.is_empty(neighbor[0],neighbor[1]):   
                    min_cell = (neighbor[0],neighbor[1])
                    min_distance = human_distance_field[neighbor[0]][neighbor[1]]
            #print 'zombie', zombie
            self._zombie_list.remove(zombie)
            self._zombie_list.append(min_cell)  
    
    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        return ans    
    
    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))
        if (row > 0) and (col < self._grid_width - 1):
            ans.append((row - 1, col + 1))
        if (row < self._grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))
        if (row < self._grid_height - 1) and (col < self._grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans  
    
    def print_df(self, dfld):
        '''
        helper prints distance field df
        '''
        for row in range(self._grid_width):
            for col in range(self._grid_height):
                print dfld[row][col],
            print
            
    
    
    
    
    
   
# TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 20))

def run_test():
    '''
    test stuff
    '''
    print 'Running basic tests'
    #apocalypse = Apocalypse(5, 5)
    #print apocalypse
    
    #apocalypse.add_zombie(0,4)
    #apocalypse.add_zombie(0,0)
    #apocalypse.add_zombie(2,3)
    #apocalypse.add_zombie(0,1)
    #print 'number of zombies = ', apocalypse.num_zombies()
    
    #apocalypse.add_human(2,2)
    #print 'number of humans = ', apocalypse.num_humans()
    
    #print 'str'
    #print apocalypse
    
    #for zombie in apocalypse.zombies():
    #    print 'zombie', zombie

    #for human in apocalypse.humans():
    #    print 'human', human        
    
    #print 'compute_distance_field', apocalypse.compute_distance_field(HUMAN)
    #print 'compute_distance_field', apocalypse.compute_distance_field(ZOMBIE) 
    #print 'compute_distance_field', apocalypse.compute_distance_field(ZOMBIE) 
    #print 'compute_distance_field', apocalypse.compute_distance_field(ZOMBIE) 
    #print 'compute_distance_field', apocalypse.compute_distance_field(ZOMBIE) 
    #print 'compute_distance_field', apocalypse.compute_distance_field(ZOMBIE) 
    #print 'compute_distance_field', apocalypse.compute_distance_field(ZOMBIE) 
    #print apocalypse
    
    #print 'compute_distance_field', apocalypse.compute_distance_field(HUMAN)
    #print apocalypse
    #print 'compute_distance_field', apocalypse.compute_distance_field(HUMAN)
    #print apocalypse 
    
    #print 'move humans', apocalypse.move_humans(apocalypse.compute_distance_field(ZOMBIE))
    #print 'move zombies', apocalypse.move_zombies(apocalypse.compute_distance_field(HUMAN))

    obj = Apocalypse(3, 3, [(0, 0), (0, 1), (0, 2), (1, 0)], [(2, 1)], [(1, 1)])
    dist = [[9, 9, 9], [9, 1, 2], [1, 0, 1]]
    obj.move_humans(dist)
    print obj
    
    #expected location to be one of [(1, 2)] but received (0, 1) 
    
#run_test()



