"""
Analyzing a simple dice game

JRO - 15/06/2015


Walking on a busy street, you happen upon a stranger sitting at a small folding
table and holding three dice. He is pitching the following game to the surrounding 
crowd: give him $10 and he will let you roll the dice. If you roll doubles (two
of the dice are paired), he will return your $10. If you roll triples (all three
dice have the same value), he will give you $200. However, if you roll neither (the 
dice are unpaired), he keeps your $10. Although the lure of $200 is tempting, you
are wise and move on. Later that evening your curiosity gets the best of you and
you decide to use your math/Python skills to analyze the game and determine whether
the game (if it is legitimate) is in your favor.

Our task in analyzing this game is to compute the expected value of a single round
of the game. To compute this value, we need to determine how likely rolling doubles
and triples are using three dice. After paying our initial $10, our expected return
will be the probability of rolling doubles times $10 plus the probability of rolling
triples times $200. If the resulting expected return is greater than $10, you should
have played (as long as you had a bodyguard). Your task for this activity is to build
a short Python program that computes this quantity. 

"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for _ in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

# example for digits


def max_repeats(seq):
    """
    Compute the maxium number of times that an outcome is repeated
    in a sequence
    """
    seq_list = list(seq) 
    print seq_list

    return 0


def compute_expected_value():
    """
    Function to compute expected value of simple dice game
    """

    
    return 0


def run_test():
    """
    Testing code, note that the initial cost of playing the game
    has been subtracted
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    print "All possible sequences of three dice are"
    print gen_all_sequences(outcomes, 3)
    print
    print "Test for max repeats"
    print "Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2))
    print "Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2))
    print "Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3))
    print
    print "Ignoring the initial $10, the expected value was $", compute_expected_value()
    
run_test()

