'''
notes for homework week 4
using combinations formula

storage: 
http://www.codeskulptor.org/#user40_X2u1DjH2oy_0.py




'''


import math

print '\n' * 4


def permutations(m, n):
    return float(math.factorial(m)) / float((math.factorial (m - n)))

def combinations(m, n):
    return float(math.factorial(m)) / float((math.factorial (m - n) * math.factorial(n)))

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




#m = 3  # size of set of outcomes
#n = 2  # number of combinations
#print combinations(m, n)
#print 'permtations ', permutations(10, 5)





def q4():
    '''
    Question 4
    Given a trial in which a decimal digit is selected from the list
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] with equal probability 
    0.1, consider a five-digit string created by a sequence of such trials
    (leading zeros and repeated digits are allowed). What is the probability
    that this five-digit string consists of five consecutive digits in either
    ascending or descending order (e.g; "34567" or "43210") ?

    Enter your answer as a floating point number with at least four significant
    digits of precision.

    ans = 0.8456

    '''

    def permutations(m, n):
        return float(math.factorial(m)) / float((math.factorial (m - n)))

    def combinations(m, n):
        return float(math.factorial(m)) / float((math.factorial (m - n) * math.factorial(n)))



    print
    print 'question 4 ='

    '''
    outcomes:
    01234
    12345
    23456
    34567
    45678
    56789
    and back = 6 x 2 = 12    
    '''
    m = 10
    n = 5

    all_sequences = gen_all_sequences([0,1,2,3,4,5,6,7,8,9], 5)
    all_permutations = gen_permutations([0,1,2,3,4,5,6,7,8,9], 5)
    #print all_sequences
    #print all_permutations
    print
    #print 'len of sequences    = ', len(all_sequences)
    #print 'len of permutations = ', len(all_permutations)
    #print
    #print 'calculated num of permutations = ', permutations(10, 5) 
    #print 'calculated num of combinations = ', combinations(10, 5) 
    #print
    #p = permutations(10, 5)
    #print 'permutations 10 digits 5 digit strings =', permutations(10, 5)
    #permutations = math.factorial(m) / (math.factorial(m - n) * math.factorial(n))
    #print 'possible permutations of five from 10 = ', permutations
    #print '12 possible outcomes'

    #n = 5.0
    #m = 12.0
    #print math.factorial(m) / ( math.factorial(m - n) * math.factorial(n))

    #print 'calculated:', 12 / combinations(10, 5)  

    print 'permutations 10 digits 5 digit strings =', permutations(10, 5)
    print 'combinations 10 digits 5 digit strings =', combinations(10, 5)

    all_sequences = gen_all_sequences([0,1,2,3,4,5,6,7,8,9], 5)
    print 'All possible outcomes of sequences of length 5 from 10 = ', len(all_sequences)
    print 'Possible outcomes = 12'
    print 'Probability = 12 /', len(all_sequences), ' = ', 12.0 / len(all_sequences)

#q4()



def q5():
    '''
    Question 5
    Permutations
    Consider a trial in which five digit strings are formed as permutations of the
    digits ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].
    (In this case, repetition of digits is not allowed.) If the probability of each
    permutation is the same, what is the probability that this five digits string
    consists of consecutive digits in either ascending or descending order
    (e.g; "34567" or "43210") ?

    Enter your answer as a floating point number with at least four significant digits of precision.
    '''
    print
    print 'question 5 Permutations'
    def permutations(m, n):
        return float(math.factorial(m)) / float((math.factorial (m - n)))

    def combinations(m, n):
        return float(math.factorial(m)) / float((math.factorial (m - n) * math.factorial(n)))

    all_permutations = gen_permutations([0,1,2,3,4,5,6,7,8,9], 5)
    print 'All possible npermutations = ', len(all_permutations)
    print 'Possible outcomes = 12'
    print 'Probability = 12 /', len(all_permutations), ' = ', 12.0 / len(all_permutations)
#q5()




def q8():
    '''
    If the set T has n members, how many distinct sets S are subsets of T?
    You may want to figure out the answer for a few specific values of n first.
    Enter the answer below as a math expression in n.
    '''
    print
    print "question 8"
    n = 1.0
    m = 3.0



    ans = float(math.factorial(n) / (math.factorial(n) * math.factorial(m - n))) 
    print 'T has', n , 'members and', ans, 'distinct subsets'
q8()


def q9():
    '''
    Question 9
    Combinations
    Given a standard 52 card deck of playing cards, what is the probability of being 
    dealt a five card hand where all five cards are of the same suit?

    Hint: Use the formula for combinations to compute the number of possible five card
    hands when the choice of cards is restricted to a single suit versus when the
    choice of cards is unrestricted.

    Compute your answer in Python using math.factorial and enter the answer below 
    as a floating point number with at least four significant digits of precision.
    '''
    print
    print "question 9"
    '''
    The total number of five-card hands from an ordinary deck of cards is 52 choose 5 
    = 52! / (5!(52 - 5)!) = 2,598,960
    '''
    print 'The total number of five-card hands from an ordinary deck of cards is:'
    print float(math.factorial(52) / ( math.factorial(5) * math.factorial(52 - 5)))
    print 'or using permutation function:', permutations(52, 5)
    print 'total number of five card hands of same suite'
    '''
    1st card can be any one of the 52 cards: 52/52 
    2nd card: 12/51 
    3rd card: 11/50 
    4th card: 10/49 
    5th card: 9/48 
    '''
    print (52.0/52.0)*(12.0/51.0)*(11.0/50.0)*(10.0/49.0)*(9.0/48.0)
    print 'was 0.0001981 using excel'
#q9()

        















