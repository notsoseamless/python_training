'''
    Algorithmic Thinking

    This is implementation af Algorithm_1;ER
    from psudocode in homework-1 question 10 for an algorithm for generating 
    random undirected graphs

    Used for Homework 1, Questions 10 to 16

    John Oldman - September 2015  

'''

import random



def algorithm_er(n, p):
    '''
    Input: Number of nodes n; prpbablility p
    Output: A graph g = (V,E) where g is an eleemnt of G(n,p)
    '''

    def validate(i, j):
        ''' private helper to validate in list comprehension '''
        if i != j:
            a = random.random()
            if a < p:
                return True
        return False

    V = set([node for node in range(n)]) 
    E = set([(i, j) for i in range(n) for j in range(i, n) if validate(i, j)])    

    #print 'Nodes = ', len(V), 'Edges =', len(E)
    #return ((V),(E)) 
    return len(E)


def make_adj_list():
    ''' build an adjacency list of g '''
    pass



def make_adj_matrix():
    ''' build an adjacency matrix of g '''
    pass





def simple_tests():
    ''' test function '''
    total = 0
    p = 0.5
    n = 10
    test_size = 1000

    for _ in range(test_size):
        total += algorithm_er(n, p)
    print 'aevrage =', total / test_size


    #print algorithm_er(10, 1)
    #print algorithm_er(4, 1)
    #print algorithm_er(4, 2)

    #xx = set(((1,2),(2,1),(4,5)))
    #print 'xx', xx
    #yy = set(((8,2),(9,3),(4,5)))
    #print 'yy', yy
    #print 'zz', yy.union(xx)


simple_tests()






