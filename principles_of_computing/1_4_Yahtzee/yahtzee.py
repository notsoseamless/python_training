"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level

JRO 20/06/2015
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)
#import poc_holds_testsuite



def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """    
    answer_set = set([()])
    for _ in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """    
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)


def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    ans = set([()])    
    for _ in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    hand: full yahtzee hand
    Returns an integer score 
    """
    ans = {}
    for dice in hand:
        ans[dice] = ans.get(dice, 0) + dice
    #return score[max(score, key=lambda index: score[index])] 
    return get_max_value(ans)


def get_max_value(score_data):
    '''
    helper returns max value in dictionary
    '''
    vals=list(score_data.values())
    keys=list(score_data.keys())
    return score_data[keys[vals.index(max(vals))]]


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected values)
    """
    print 'expected_value called with', held_dice, num_die_sides, num_free_dice
    outcomes = [num  for num in range(1, num_die_sides + 1)]
    all_sequences = gen_all_sequences(outcomes, num_free_dice)
    print 'all sequences ', gen_all_sequences(outcomes, num_free_dice)
    # step through each sequence
    total = 0.0   
    for hand in all_sequences:
        total += score(held_dice + hand)
    return total / len(all_sequences)


#def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
#    result = [[]]
#    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
#        result.extend([subset + [x] for subset in result])
#    return result
#def powerset(s):
#    return frozenset(map(frozenset, list_powerset(list(s))))
#def list_powerset2(lst):
#    return reduce(lambda result, x: result + [subset + [x] for subset in result],
#                  lst, [[]])
 

def powersetlist(s_data):
    '''
    returns powet sets in s_data
    '''
    res = [[]]
    for element in s_data:
        #print "res: %-55r element: %r" % (res, element)
        res += [xxx + [element] for xxx in res]
    return res
 

#def subsets(my_set):
#    result = [[]]
#    for x in my_set:
#        result = result + [y + [x] for y in result]
#    return result


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    hand: full yahtzee hand
    Returns a set of tuples, where each tuple is dice to hold
    """       
    powerset = powersetlist(hand)
    #powerset = list_powerset(hand)
    powerset = [tuple(sorted(sequence)) for sequence in powerset]
    #print set(powerset)
    return set(powerset)   
  


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die
    

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    print 'hand', hand
    all_holds = gen_all_holds(hand)
    print 'all_holds', all_holds
    
    high_score = 0
    high_hold = 0
    for held_dice in all_holds:
        print 'holding', held_dice, 'free dice', len(hand) - len(held_dice)
        num_free_dice = len(hand) - len(held_dice)
        d_score = expected_value(held_dice, num_die_sides, num_free_dice)
        #print 'd_score', d_score
        if d_score > high_score:
            high_score = d_score
            high_hold = held_dice
 
    return (high_score, high_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    #num_die_sides = 6
    #hand = (1, 1, 1, 5, 6)
    #hand_score, hold = strategy(hand, num_die_sides)

    #print expected_value( () , 6, 2 )
    #print expected_value( (2,2) , 6, 2 )
    #print expected_value( (3,3) , 8, 5 )
    #print expected_value( (2,2) , 2, 1 )
    
#   print gen_all_holds((1, 2, 2, 3))
#    print gen_all_holds((1, 4))

#    print sort_tuples((2, 1))
#    print sort_tuples((3, 2, 1))
#    print sort_tuples((4, 3, 2, 1))
#    print sort_tuples((5, 4, 3, 2, 1))

    hand = (1, 2, 2, 3)
    hand = (1,)

    print strategy(hand, 6) 
    

    #print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()



#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    


