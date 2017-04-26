

import math


def add_up(n):
    '''
    q2
    If n is non-negative integer, enter a math expression in n 
    for the value returned by add_up(n).

    0 + 1 + 2 + 3 + ... + n

    '''
    if n == 0:
        return 0
    else:
        return n + add_up(n - 1)

#print 'Q2'
#for n in range(10):
#    print add_up(n),
#    print '            ', (n * (n + 1))/2 
#print '\n\n'


def multiply_up(n):
    '''
    q3
    If n is non-negative integer, enter a math expression in n for the value
    returned by multiply_up(n).
    '''
    if n == 0:
        return 1
    else:
        return n * multiply_up(n - 1)

#print 'Q3'
#for n in range(10):
#    print multiply_up(n),
#    print '              ', math.factorial(n)
#print '\n\n'


count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
def fib(num):
    '''
    q4
    Let f(n) be the total number of calls to the function fib that are 
    computed during the recursive evaluation of fib(n). Which recurrence
    reflects the number of times that fib is called during this evaluation of fib(n)?

    You may want to add a global counter to the body of fib that records the number
    of calls for small values of n.
    '''
    global count_0
    global count_1
    global count_2
    global count_3
    
    count_0 += 1

    if num == 0:
        count_1 += 1
        return 0
    elif num == 1:
        count_2 += 1
        return 1
    else:
        count_3 += 1
        return fib(num - 1) + fib(num - 2)

def test_q4():
    print 'Q4'
    for n in range(0, 10):
        print fib(n),
        print '       ', (n - 1) + (n - 2) + 1,
        print '       ', 2 * (n - 1) + 1,
        print '       ', (n - 1) + 1,
        print '       ', (n - 1) + (n - 2), 
        print '       counts all', count_0,  '   f(0)',count_1, '   f(1)', count_2, '   f(n)', count_3
    print '\n\n'

    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for n in range(0, 30):
            fib(n)
            print count_0

    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0


def fib_count(num):
    '''
    q4
    Let f(n) be the total number of calls to the function fib that are 
    computed during the recursive evaluation of fib(n). Which recurrence
    reflects the number of times that fib is called during this evaluation of fib(n)?

    You may want to add a global counter to the body of fib that records the number
    of calls for small values of n.
    '''
    global count_0
    global count_1
    global count_2
    global count_3
    
    count_0 += 1

    if num == 0:
        count_1 += 1
        return 0
    elif num == 1:
        count_2 += 1
        return 1
    else:
        count_3 += 1
        return fib(num - 1) + fib(num - 2)





count_mfib = 0
def memoized_fib(num, memo_dict):
    '''
    q5
    The number of recursive calls to fib in the previous problem grows quite quickly.
    The issue is that fib fails to "remember" the values computed during previous
    recursive calls. One technique for avoiding this issue is memoization,
    a technique in which the values computed by calls to fib are stored in 
    an auxiliary dictionary for later use.

    The Python function below uses memoization to compute the Fibonacci numbers efficiently. 
    
    If n > 0, how many call to memoized_fib are computed during the evaluation of
    the expression memoized_fib(n, {0 : 0, 1 : 1})? Enter the answer as a math 
    expression in n below.

    You may want to add a global counter to the body of fib keeps track of the 
    number of calls so that you can track the number of recursive calls.  
    '''
    global count_mfib

    count_mfib += 1

    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

def test_memoized_fib():
    print '\n\n\nQ5'
    for n in range(1, 20):
        memoized_fib(n, {0 : 0, 1 : 1}) 
        print count_mfib

test_memoized_fib()



# Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6  Q6 
'''
guys, you just need to write recursively the function gen_all_sequences 
from Yahtzee game (1-st part of the course), to find the answer.
'''
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def rec_gen_all_sequences(outcomes, length):
    """
    recursive function that enumerates the set of all sequences of
    outcomes of given length.

    Given a list outcomes of length n, we can perform the following recursive 
    computation to generate the set of all permutations of length n:

        Compute the set of permutations rest_permutations for the list outcomes[1 :]
        of length n-1,

        For each permutation perm in rest_permutations, insert outcome[0] at each possible
        position of perm to create permutations of length n,

        Collect all of these permutations of length n into a set and return that set.
    """    
#    if outcomes == []:
#        return outcomes
#    else:
#        rest_permutations = outcomes[1 :]
#        rec_gen_all_sequences(outcomes[1 :], length-1) for perm in rest_permutations]##

#        for perm in rest_permutations:
#            # insert outcome[0] at each possible position of perm to create permutations of length n,

#            rest_permutations = rec_gen_all_sequences(outcomes[1 :], length-1)
#            print rest_permutations
            
#            return rest_permutations

    if outcomes == []:
        return outcomes
    else:
        for i in range(length - 1):
            for perm in rec_gen_all_sequences(outcomes[1 :], length - 1 ):
                return outcomes 




        # return rec_gen_all_sequences(outcomes[1 :], length-1)
        #rest_permutations = rec_gen_all_sequences(outcomes[1 :], length-1)
        #return rest_permutations




def test_q6():
    outcomes = [1,2]
    length = 2
    print '\n\n\nQ6'
    print 'iterative'
    print gen_all_sequences(outcomes, length)
    print '\nrecursive'
    print rec_gen_all_sequences(outcomes, length)
    print '\n\n\n'

##test_q6()







