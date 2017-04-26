"""
Iterative program to print out Pascal's triangle
"""

import math

TRIANGLE_HEIGHT = 10

def next_line(current_line):
    """
    Given a line in Pascal's triangle, generate the following line

    Question:
    Enter a math expression in m and n using factorial (!) that represents 
    the value of the nth entry of the mth row of Pascal's triangle. 
    (Both the row numbers and entry numbers are indexed starting at zero.)

    """
    
    ans = [1]
    
    for idx in range(len(current_line) - 1):
        ans.append(current_line[idx] + current_line[idx + 1])
    
    ans.append(1)
    
    return ans

def run_example():
    # code to print out Pascal's triangle
    pascal_line = [1]	# row zero
    print pascal_line
    
    for dummy_idx in range(TRIANGLE_HEIGHT - 1):
        pascal_line = next_line(pascal_line)
        print pascal_line


def run_example_one(row, col):
    '''
             m!
    ans = -----------
          n! (m - n)!

    entered as m!/(n!(m-n)!)

    '''
    ans =  math.factorial(row) / ( math.factorial(col) * math.factorial(row - col))
    print 'row ', row, ' col ', col, '  ', ans 



run_example()

run_example_one(52, 5)



    
    

