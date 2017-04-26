"""
Test suite for TwentyFortyEight class
"""

import poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def run_suite(TwentyFortyEight):
    """
    Some informal testing code
    """
    
    print 'Running test suite'   
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # create a 2048 game object
    height = 4
    width = 4
    game = TwentyFortyEight(height, width)
     
    # test the initial configuration of the grid using the str method
    suite.run_test(str(game), str(), "Test #0: init")
 
    # test getter methods
    suite.run_test(game.get_grid_height(), height, 'Test #1 get_grid_height')
    suite.run_test(game.get_grid_width(), width, 'Test #2 get_grid_width')        

    #test set/get method
    for col in range(width):
        for row in range(height):
            suite.run_test(game.set_tile(3,3,row*col), None, 'Test #3 set_tile()')
            suite.run_test(game.get_tile(3,3), row*col, 'Test #4 get_tile()')



    # owl test failures
    suite.run_test(game.set_tile(0, 0, 2), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(0, 1, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(0, 2, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(0, 3, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 0, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 1, 2), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 2, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 3, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 0, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 1, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 2, 2), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 3, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 0, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 1, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 2, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 3, 2), None, 'Test #4 set_tile()')

    suite.run_test(str(game), str(), "Test #0: init")
    
    suite.run_test(game.move(UP), None, 'Test #5 move()')
    #suite.run_test(game.move(DOWN), None, 'Test #5 move()')
    #suite.run_test(game.move(LEFT), None, 'Test #5 move()')
    #suite.run_test(game.move(RIGHT), None, 'Test #5 move()')
    #suite.run_test(game.move(UP), None, 'Test #5 move()')
   
    suite.run_test(str(game), str(), "Test #0: init")



      # owl test failures
    suite.run_test(game.set_tile(0, 0, 2), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(0, 1, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(0, 2, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(0, 3, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 0, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 1, 2), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 2, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(1, 3, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 0, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 1, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 2, 2), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(2, 3, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 0, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 1, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 2, 0), None, 'Test #4 set_tile()')
    suite.run_test(game.set_tile(3, 3, 2), None, 'Test #4 set_tile()')

    suite.run_test(str(game), 'Before', "Test #0: init")
    
    suite.run_test(game.move(DOWN), None, 'Test #5 move()')
  
    suite.run_test(str(game), 'After', "Test #0: init")
   





    
    
    suite.report_results()
    

