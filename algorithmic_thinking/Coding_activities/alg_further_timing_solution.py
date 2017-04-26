"""
Time trial code for comparing range vs. xrange

Test in IDLE, then CodeSkulptor
"""

import time

#import codeskulptor
#codeskulptor.set_timeout(20)

def sum_range(x):
    """
    Test function for range
    """
    sum = 0
    for i in range(x+1):
        sum = sum + i
    return sum

def time_sum_range(x):
    """
    Timing code for range
    """
    start = time.time()
    result = sum_range(x)
    stop = time.time()
    elapsed = stop - start
    return elapsed

def sum_xrange(x):
    """
    Test function for xrange
    """
    sum = 0
    for i in xrange(x+1):
        sum = sum + i
    return sum

def time_sum_xrange(x):
    """
    Timing code for xrange
    """
    start = time.time()
    result = sum_xrange(x)
    stop = time.time()
    elapsed = stop - start
    return elapsed

def time_trial(sum_to, num_trials):
    """
    Compare range vs. xrange
    """

    for i in xrange(num_trials):
        range_result = time_sum_range(sum_to)
        xrange_result = time_sum_xrange(sum_to)
        delta = range_result - xrange_result
        print 'range =  ' + str(range_result)
        print 'xrange = ' + str(xrange_result)
        print 'xrange faster by: ' + str(delta) + ' seconds.'

time_trial(10000000, 5)

