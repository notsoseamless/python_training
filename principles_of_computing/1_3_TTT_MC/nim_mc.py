"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game

Nim (Monte Carlo) 
"""

import random
try:
    import codeskulptor
    codeskulptor.set_timeout(20)
except:
    print 'not in codeskulptor'


# globals
MAX_REMOVE = 3
TRIALS = 10000


def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim

    STRATERGY
    =========
    For each possible initial move, make the given move (that is decrement 
    num_items the specified amount),
    
    
    
    Finally, choose the initial move that leads to the highest fraction of random games won.


    """
    
    #Play TRIALS games of Nim using randomly generated moves,
    initial_moves = []
    for _ in range(TRIALS):
        current_items = num_items
        initial_move = random.randint(1, MAX_REMOVE)
        current_items -= initial_move 
        while current_items > 0:
            comp_move = random.randint(1, MAX_REMOVE)
            current_items -= comp_move
            if current_items <= 0:
                initial_moves.append(initial_move)
            player_move = random.randint(1, MAX_REMOVE)
            current_items -= player_move
    
   
    #Compute the fraction of games won for that initial move,
    # find best of the three moves
    # use list of lists of [move , number of times]
    best_moves = [[number + 1, 0] for number in range(MAX_REMOVE)]
    for index in range(MAX_REMOVE):
        for move in range(len(initial_moves)):
            if initial_moves[move] == index + 1:
                best_moves[index][1] += 1
    #print best_moves
        
    # sort list by last element for highest scoring squares  
    best_moves = sorted(best_moves, reverse=True, key=lambda x: x[1])    
    print best_moves
    return best_moves[0][0]


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move "))
        # limit player input
        if player_move > MAX_REMOVE:
            print 'Error - limiting to ', MAX_REMOVE
            player_move = MAX_REMOVE
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(21)
        
    
                 
    

