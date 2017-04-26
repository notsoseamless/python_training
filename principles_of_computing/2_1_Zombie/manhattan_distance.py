"""
An example of creating a distance field using Manhattan distance

jro 14/07/2015

"""

GRID_HEIGHT = 6
GRID_WIDTH = 8


def manhattan_distance(row0, col0, row1, col1):
    """
    Compute the Manhattan distance between the cells
    (row0, col0) and (row1, col1)
    """
    return abs(row1 - row0) + abs(col1 - col0)
        

def create_distance_field(entity_list):
        """
        Create a Manhattan distance field that contains the minimum distance to 
        each entity (zombies or humans) in entity_list
        Each entity is represented as a grid position of the form (row, col) 
        """

        def get_distance(row, col):
            '''
            manages distance calculations
            '''
            dist1 = manhattan_distance(row, col, entity_list[0][0], entity_list[0][1]) 
            dist2 = manhattan_distance(row, col, entity_list[1][0], entity_list[1][1]) 
            if dist1 < dist2:
                return dist1
            else:
                return dist2

        grid = []
        for row in range(GRID_HEIGHT):
            temp_row = []
            for col in range(GRID_WIDTH):
                temp_row.append(get_distance(row, col))
            grid.append(temp_row)
        return grid
   


    
def print_field(field):
    """
    Print a distance field in a human readable manner with 
    one row per line
    """
    for row in range(GRID_HEIGHT):
        print '[',
        for col in range(GRID_WIDTH):
            print field[row][col],',',
        print ']\n'




def run_example():
    """
    Create and print a small distance field
    """
    field = create_distance_field([[4, 0],[2, 5]])
    print_field(field)
    
run_example()


# Sample output for the default example
#[4, 5, 5, 4, 3, 2, 3, 4]
#[3, 4, 4, 3, 2, 1, 2, 3]
#[2, 3, 3, 2, 1, 0, 1, 2]
#[1, 2, 3, 3, 2, 1, 2, 3]
#[0, 1, 2, 3, 3, 2, 3, 4]
#[1, 2, 3, 4, 4, 3, 4, 5]
    
    

