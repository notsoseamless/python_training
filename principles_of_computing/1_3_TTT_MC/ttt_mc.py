"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided
#import user40_AMu2IY1JvM_45 as TestSuite
#import  tic_tac_toe_monty_carlo_test.py as TestSuite


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 5         # Number of trials to run
SCORE_CURRENT = 2.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player


def mc_trial(board, player):
    '''
    This function takes a current board and the next player to move. 
    The function should play a game starting with the given player
    by making random moves, alternating between players. 
    The function should return when the game is over.
    The modified board will contain the state of the game, 
    so the function does not return anything. 
    In other words, the function should modify the board input.
    '''
    while board.check_win() == None:
        # game not over
        empty_squares = board.get_empty_squares()
        # choose next square
        next_move = random.choice(empty_squares)
        # make the move
        board.move(next_move[0], next_move[1], player)
        # switch the player
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    '''
    This function takes a grid of scores (a list of lists) with the 
    same dimensions as the Tic-Tac-Toe board, a board from a completed
    game, and which player the machine player is. The function should
    score the completed board and update the scores grid. As the function
    updates the scores grid directly, it does not return anything,
    '''              
    if board.check_win() != provided.DRAW:
        # scoring = [DRAW, PLAYERX, PLAYERO]
        if player == provided.PLAYERO:
            # curernt player is O
            if board.check_win() == provided.PLAYERO:              
                scoring = [0, -SCORE_OTHER, SCORE_CURRENT]
            else:
                scoring = [0, SCORE_OTHER, -SCORE_CURRENT]
        else:
            # current player is X
            if board.check_win() == provided.PLAYERX:
                scoring = [0, SCORE_OTHER, -SCORE_CURRENT]
            else:
                scoring = [0, -SCORE_OTHER, SCORE_CURRENT]  
        # traverse the board
        size = board.get_dim()
        for row in range(size):
            for col in range(size):
                #print row, col, board.square(row, col)
                scores[row][col] += scoring[board.square(row, col)-1]
   

    
def get_best_move(board, scores): 
    '''
    This function takes a current board and a grid of scores. The function
    should find all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple.
    It is an error to call this function with a board that has no empty squares
    (there is no possible next move), so your function may do whatever it wants
    in that case. The case where the board is full will not be tested.
    '''
    # get list of empty squares
    empty_squares = board.get_empty_squares()
    #print 'empty_squares ', empty_squares
    if len(empty_squares) > 0:
        # append the score
        empty_square_scores = []
        for index in range(len(empty_squares)):
            score = scores[empty_squares[index][0]][empty_squares[index][1]]
            # add scores to empty squares
            empty_square_scores.append(empty_squares[index] + (score,))
        #print 'empty_square_scores ', empty_square_scores
                  
        # sort list by last element for highest scoring squares  
        empty_square_scores = sorted(empty_square_scores, reverse=True, key=lambda x: x[2])    
        #print 'empty_square_scores ', empty_square_scores
    
        # highest score ts ad beginning of list
        highest_score = empty_square_scores[0][2]                
        top_scores = [empty_square_scores[index]  for index in range(len(empty_square_scores)) \
                               if empty_square_scores[index][2] == highest_score]
        #print 'top_scores ', top_scores
        suggested_move = random.choice(top_scores)
        # return the tuple less the score
        return (suggested_move[0], + suggested_move[1])
    


def mc_move(board, player, trials): 
    '''
    This function takes a current board, which player the machine player is, and
    the number of trials to run. The function should use the Monte Carlo simulation
    described above to return a move for the machine player in the form of a (row, column)
    tuple. Be sure to use the other functions you have written!
    '''

    # build scores list
    size = board.get_dim()
    scores = [[0 for _ in range(size)] for _ in range(size)]
    
    for _ in range(trials):
        # run trial games
        clone = board.clone()
        mc_trial(clone, player)  
        # gather scores
        mc_update_scores(scores, clone, player)
        
        best_move = get_best_move(board, scores)
    print 'suggester move ', best_move
   
    return best_move
   
    


            


def test_ttt(size):
    ''' simple etst suite '''
    
    print 'Running test suite' 
    #print 'EMPTY  ', provided.EMPTY
    #print 'PLAYERX', provided.PLAYERX
    #print 'PLAYERO', provided.PLAYERO
    #print 'DRAW   ', provided.DRAW

    #board = provided.TTTBoard(3)
    #print board
    #print board.get_dim()
    #player = provided.PLAYERX
    #print player
    #player = provided.switch_player(player)
    #print player    
    #print dir(provided)
    #print dir(provided.TTTBoard)    
    #print provided.TTTBoard.get_empty_squares(board)    


    # build scores list
    #scores = [[0 for _ in range(size)] for _ in range(size)]

    #for _ in range(100):
    #    # create a board object
    #    board = provided.TTTBoard(size)    
    #    # run game
    #    mc_trial(board, provided.PLAYERO)    
    #    # gather scores
    #    player = provided.PLAYERX 
    #    mc_update_scores(scores, board, player)
    #print 'scores ',scores      

    #best_move = get_best_move(board, scores)
    #print best_move
    
    
    board = provided.TTTBoard(3)
    trials = 100
    print board
    player = provided.PLAYERO
    while board.check_win() == None:
       # game not over
       # choose next square
       next_move = mc_move(board, player, trials)
       # make the move
       board.move(next_move[0], next_move[1], player)
       # switch the player
       player = provided.switch_player(player)
       print board
    
    
    
    
    
    
    
    
    
    
    

#TestSuite.run_suite(mc_trial)
#TestSuite.run_suite(mc_update_scores)

#test_ttt(3)





# Test game with the console or the GUI.  Uncomment whichever
# you prefer. Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)



