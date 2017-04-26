"""
Merge function for 2048 game.

Written by John Oldman 25/05/2015
Mini project for Coursera Principles of Computing

"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # retain length of input for later
    original_line_length = len(line)

    def pack_line(line):
        '''
        Iterate over the line and return a list that has all the
        non-zero tiles slid over to the beginning of the list
        '''
        return [cell for cell in line if cell]


    # pack the line
    line = pack_line(line)

    # merge equal pairs (x2)
    for index in range(len(line)-1):
        if line[index] == line[index + 1]:
            # merge the two indexes
            line[index] *= 2
            # clear the old index
            line[index + 1] = 0

    # repack the line
    line = pack_line(line)

    # pad original list length with zeros
    line += ([0 for index in range(len(line), original_line_length)])

    return line



def run_test():
    '''
    test code to test merge
    '''
    print 'Test with [2, 0, 2, 4] =', str(merge([2, 0, 2, 4])), 'expecting [4, 4, 0, 0]'
    print 'Test with [0, 0, 2, 2] =', str(merge([0, 0, 2, 2])), 'expecting [4, 0, 0, 0]'
    print 'Test with [2, 2, 0, 0] =', str(merge([2, 2, 0, 0])), 'expecting [4, 0, 0, 0]'
    print 'Test with [2, 2, 2, 2, 2] =', str(merge([2, 2, 2, 2, 2])), 'expecting [4, 4, 2, 0, 0]'
    print 'Test with [8, 16, 16, 8] =', str(merge([8, 16, 16, 8])), 'expecting [8, 32, 8, 0]'


run_test()


