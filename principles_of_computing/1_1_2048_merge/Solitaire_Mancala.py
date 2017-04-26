"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

import random
#import simplegui
#import poc_mancala_gui

# Game and canvas constants
# Focus on boards with six houses and one store

BOARD_SIZE = 7
HOUSE_NUM = 120
TEXT_OFFSET = [0.3 * HOUSE_NUM, 0.7 * HOUSE_NUM]
CANVAS_SIZE = [BOARD_SIZE * HOUSE_NUM, HOUSE_NUM]

# all winnable games for six houses
WINNABLE_BOARDS = [[0, 0, 0, 0, 2, 4, 6], 
                    [0, 0, 0, 2, 4, 0, 0], 
                    [0, 0, 1, 1, 3, 5, 0], 
                    [0, 0, 1, 3, 0, 0, 0], 
                    [0, 0, 1, 3, 2, 4, 6], 
                    [0, 0, 2, 0, 0, 0, 0], 
                    [0, 0, 2, 0, 2, 4, 6], 
                    [0, 0, 2, 2, 4, 0, 0], 
                    [0, 1, 0, 0, 0, 0, 0], 
                    [0, 1, 0, 0, 2, 4, 6], 
                    [0, 1, 0, 2, 4, 0, 0], 
                    [0, 1, 1, 1, 3, 5, 0], 
                    [0, 1, 1, 3, 0, 0, 0], 
                    [0, 1, 1, 3, 2, 4, 6], 
                    [0, 1, 2, 0, 0, 0, 0], 
                    [0, 1, 2, 0, 2, 4, 6], 
                    [0, 1, 2, 2, 4, 0, 0]]



class MancalaGUI:
    """
    Container for interactive content
    """    

    def __init__(self, game):
        """ 
        Initializer to create frame, sets handlers and initialize game
        """
        self._frame = simplegui.create_frame("Mancala Solitaire", 
                                            CANVAS_SIZE[0], CANVAS_SIZE[1])
        self._frame.set_canvas_background("White")
        self._frame.set_draw_handler(self.draw)
        self._frame.add_button("New board", self.new_board, 200)
        self._frame.add_button("Restart board", self.restart_board, 200)
        self._frame.add_button("Make move", self.make_move, 200)
        self._frame.set_mouseclick_handler(self.click_move)
        
        # fire up game and frame
        self._game = game
        self.new_board()
        
    def start(self):
        """
        Start the GUI
        """
        self._frame.start()
        
    def restart_board(self):
        """
        Restart the game with the current configuration
        """
        self._game.set_board(self.start_board)
                   
    def new_board(self):
        """
        Restart the game with a new winnable baord
        """
        self.start_board = random.choice(WINNABLE_BOARDS)
        self.restart_board()
    
    def make_move(self):
        """
        Compute and apply next move for solver
        """
        self._game.apply_move(self._game.choose_move())    
        
    def click_move(self, pos):
        """
        Update game based on mouse click
        """
        move = (BOARD_SIZE - 1) - pos[0] // HOUSE_NUM
        self._game.apply_move(move)    
        
    def draw(self, canvas):
        """
        Handler for draw events, draw board
        """
        configuration = [self._game.get_num_seeds(house_num) for house_num in range(BOARD_SIZE)]
        current_text_pos = [(BOARD_SIZE - 1) * HOUSE_NUM + TEXT_OFFSET[0], TEXT_OFFSET[1]]
        current_line_pos = [(BOARD_SIZE - 1) * HOUSE_NUM, 0]
        
        if self._game.is_game_won():
            store_color = "LightGreen"
        else:
            store_color = "Pink"
        
        canvas.draw_polygon([current_line_pos, 
                             [current_line_pos[0] + HOUSE_NUM, current_line_pos[1]],
                             [current_line_pos[0] + HOUSE_NUM, current_line_pos[1] + HOUSE_NUM],
                             [current_line_pos[0], current_line_pos[1] + HOUSE_NUM]], 
                            3, "Black", store_color)
        
        for num_seeds in configuration:
            canvas.draw_text(str(num_seeds), current_text_pos, 0.5 * HOUSE_NUM, "Black")
            canvas.draw_line(current_line_pos, [current_line_pos[0], 
                                                current_line_pos[1] + HOUSE_NUM], 2, "Black")
            current_text_pos[0] -= HOUSE_NUM
            current_line_pos[0] -= HOUSE_NUM

def run_gui(game):
    """
    Run GUI with given game
    """
    gui = MancalaGUI(game)
    gui.start()
        


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._mancala_board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._mancala_board = configuration
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        result = list(self._mancala_board)
        result.reverse()
        return ''.join(str(result))
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return str(self._mancala_board[house_num])

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for house in range(1,len(self._mancala_board)):
            if self._mancala_board[house]: 
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if self._mancala_board[house_num] and self._mancala_board[house_num] == house_num:
            return True
        else:
            return False

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for house in range(0, house_num):
                self._mancala_board[house] += 1
            self._mancala_board[house_num] = 0
 
    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house in range(1,len(self._mancala_board)):
            if self.is_legal_move(house):
                return house
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        result = []
        sub_game = SolitaireMancala()
        sub_game.set_board(list(self._mancala_board))
        while (not sub_game.is_game_won()) and (sub_game.choose_move() != 0):
            next_move = sub_game.choose_move()
            result.append(next_move)
            sub_game.apply_move(next_move)
        return result
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    # add more tests here
    print my_game.is_game_won()
    for n in range(1,7):
        print str(n) + '   ' + str(my_game.is_legal_move(n))
        
    print 'Move choice = ' + str(my_game.choose_move())
    
    print
    print 'plan = ' + str(my_game.plan_moves())
    
    print 'Check game is unchanged: ' + str(my_game)
    
    print 'suggest ' + str(my_game.choose_move())
    my_game.apply_move(4)
    print str(my_game)
 
test_mancala()


# Import GUI code once you feel your code is correct
#poc_mancala_gui.run_gui(SolitaireMancala())




