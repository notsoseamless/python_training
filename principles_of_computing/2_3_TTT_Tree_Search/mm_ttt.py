"""
Mini-max Tic-Tac-Toe Player

jro - 02/08/2015

"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

#COUNTER = 0

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    
    #global COUNTER
    #COUNTER += 1
    
    row = 0
    col = 0
    score = 0
    result = 0
    scores = []
    #print board
    #print 'empty cells', board.get_empty_squares()
    for move in board.get_empty_squares():
        #print 'process empty cell', move
        row = move[0] 
        col = move[1] 
        clone = board.clone()
        #print 'Before move\n', clone
        clone.move(row, col, player)
        #print 'After move\n', clone   
        winner = clone.check_win()
        if winner == provided.DRAW:
            # game is draw
            #print 'game is draw'
            score = 0
            #return 0, (-1, -1)
        elif winner == provided.PLAYERX:
            # PLAYERX wins
            #print 'PLAYERX wins'
            score = 1
            #print 'returning', score, move
            #continue
            #return score * player, move
        elif winner == provided.PLAYERO:
            # PLAYERO wins
            #print 'PLAYERO wins'
            score = -1           
            #print 'returning', score, move   
            #return score * player, move
        else:
            # game is in progress
            #print 'game in progress'
            result = mm_move(clone, provided.switch_player(player))[0]
            #print 'result', result
            score = result
        scores.append([score, move])
        #print 'scores', scores
    #print 'final return player:', print_player(player), 'score', score, 'move', move
    #return score * player, (row, col)
    #print 'choose from these scores', scores
    if player == provided.PLAYERX:
        # maximise
        #print 'returning max', max(scores)
        return tuple(max(scores))
    else:
        # minimise
        #print 'returning min', min(scores)
        return tuple(min(scores))
    
    #print clone
    #print 'final return =', score, (row, col)
    return (score, (row, col))

  
     
        
def print_player(player):
    '''
    helper ids player
    '''
    if player == provided.PLAYERX:
        print 'PLAYERX',
    elif player == provided.PLAYERO:
        print 'PLAYERO',
    else:
        print '???????????'
    




def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    #print 'move =', move
    #print 'score =', move[0]
    #print 'move =', move[1]
    #assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move
    






def test_mm_move():
    '''
    simple test
    '''
    #global COUNTER
    #COUNTER = 0
    
    board = provided.TTTBoard(3)
    #print 'dim =', board.get_dim(), '\n'
    board.move(0, 1, provided.PLAYERX)
    board.move(1, 1, provided.PLAYERX)
    board.move(2, 2, provided.PLAYERX)
    board.move(0, 0, provided.PLAYERO)
    board.move(1, 0, provided.PLAYERO)
    board.move(2, 1, provided.PLAYERO)
    #print 'provided.PLAYERO = ', provided.PLAYERO 
    #print board
    #player = provided.PLAYERX
    #print 'player =', player
    #player = provided.switch_player(player)
    #print 'player =', player    
    #print dir(provided)
    #print dir(board)    
    #print board.get_empty_squares()
    
    #print '\n\n\nRunning test suite\n'
    #print mm_move(board, player)
    

    print mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]), provided.PLAYERO)
    # expected score -1 but received (1, (1, 2))
    
    
    #print mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERO)
    #returned bad move "(Exception: Returned Type Mismatch) Expected type 'tuple' but returned type 'int'."
    
    
    #print mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX) 
    #returned bad move (0, (2, 2))

    
    #print mm_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), provided.PLAYERX)
    #expected score 1 but received (0, (1, 1))

    
    
    #print mm_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), provided.PLAYERX)     
    #returned invalid move "(Exception: Returned Type Mismatch) 
    #Expected type 'tuple' but returned type 'NoneType'."
 
    
    


test_mm_move()      

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.


#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

