'''
    Algorithmic Thinking
    Project 1 - Degree distributions for graphs 

    John Oldman - September 2015
'''

GRAPH0 = {0: set([1]),
          1: set([2]),
          2: set([3]),
          3: set([0])}

GRAPH1 = {0: set([]),
          1: set([0]),
          2: set([0]),
          3: set([0]),
          4: set([0])}

EX_GRAPH0 = {0: set([1, 2]), 
             1: set([]), 
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}



def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes. 
    A complete graph contains all possible edges subject to the restriction
    that self-loops are not allowed. 
    The nodes of the graph are numbered 0 to num_nodes - 1 when num_nodes is
    positive. Otherwise, the function returns a dictionary corresponding to 
    the empty graph.    
    '''
    complete_graph = {}
    for node_num in range(num_nodes):
        # make a node and add it to complete_graph
        complete_graph[node_num] = set([edge for edge in range(num_nodes) if edge != node_num])        
    return complete_graph



def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes
    the in-degrees for the nodes in the graph. 
    The function returns a dictionary with the same set of keys (nodes) as
    digraph whose corresponding values are the number of edges whose head 
    matches a particular node.     
    '''
    result = {}
    for node in digraph.keys():
        # initialise empty node to result
        result[node] = 0
        for edge in digraph.keys():
            if node in digraph[edge]:
                # update node count
                result[node] += 1
    return result



def in_degree_distribution(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes 
    the unnormalized distribution of the in-degrees of the graph. 
    The function returns a dictionary whose keys correspond to in-degrees of 
    nodes in the graph. 
    The value associated with each particular in-degree is the number of nodes
    with that in-degree. 
    In-degrees with no corresponding nodes in the graph are not included in the
    dictionary.    
    '''
    result = {}

    # make dict of in nodes
    in_edges = {}

    for node in digraph.keys():
        in_edges[node] = 0
        # now search all other nodes for edges into this node
        for edge in digraph.keys():
            if node in digraph[edge]:
                if node not in in_edges:
                    in_edges[node] = 1
                else:
                    in_edges[node] += 1

    # now count numbers of in_edges 
    for counts in in_edges.keys():
        if in_edges[counts] not in result:
            result[in_edges[counts]] = 1
        else:
            result[in_edges[counts]] += 1
    return result



def simple_test():
    '''
    test code
    '''
    print 'Running Tests'
    print '============='

    print '\nTesting make_complete_graph'
    print make_complete_graph(0)
    print make_complete_graph(1)
    print make_complete_graph(2)
    print make_complete_graph(3)
    print make_complete_graph(9)

    print'\nTesting compute_in_degrees'
    print compute_in_degrees(GRAPH0)
    #print compute_in_degrees(EX_GRAPH1)
    #print compute_in_degrees(EX_GRAPH2)


    # in_degree_distribution(alg_module1_graphs.GRAPH0) expected {1: 4} but received {} 
    # (Exception: Invalid Keys) Expected dictionary {1: 4} has a different number of keys 
    # than received dictionary {}

    #in_degree_distribution(alg_module1_graphs.GRAPH1) 
    print '\n\nexpected {0: 4, 4: 1} but received {0: 1, 1: 4}'


    print'\nTesting in_degree_distribution'
    #print in_degree_distribution(GRAPH0)
    print in_degree_distribution(GRAPH1)
    #print in_degree_distribution(EX_GRAPH0)
    #print in_degree_distribution(EX_GRAPH1)
    #print in_degree_distribution(EX_GRAPH2)



# run the tests
simple_test()

