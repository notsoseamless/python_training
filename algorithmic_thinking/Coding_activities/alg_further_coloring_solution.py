"""
Solution for "Graph coloring" for Further activities

Note that this solution requires itertools and 
should be run on desktop Python
"""

import itertools

# Examples graphs

GRAPH1 = {0: set([1, 2]),
      1: set([0, 2]),
      2: set([0, 1])}

GRAPH2 = {0: set([1, 2, 3]),
      1: set([0, 2, 3]),
      2: set([0, 1, 3]),
      3: set([0, 1, 2])}

GRAPH3 = {0: set([1, 2, 4, 5]),
      1: set([0, 2, 3, 5]),
      2: set([0, 1, 3, 4]),
      3: set([1, 2, 4, 5]),
      4: set([0, 2, 3, 5]),
      5: set([0, 1, 3, 4])}

GRAPH4 = {1: set([2, 8]),
      2: set([1, 3, 4, 6, 8]), 
      3: set([2, 4]), 
      4: set([2, 3, 5, 6, 8]), 
      5: set([4, 6]), 
      6: set([2, 4, 5, 7, 8]), 
      7: set([6, 8]), 
      8: set([1, 2, 4, 6, 7])}


def has_internal_edge(g, nodeset):
    """
    Check if any pair of nodes in the set nodeset has an
    edge connecting them in g.

    Arguments:
    g -- undirected graph
    nodeset -- subset of nodes in g

    Returns:
    True if there is an edge between any two nodes in nodeset, 
    False otherwise.
    """
    for node in nodeset:
        for nbr in g[node]:
            if nbr in nodeset:
                return True
    return False

def is_three_colorable(g):
    """
    Check if g is three colorable.

    Arguments:
    g -- undirected graph

    Returns:
    True if there is a three coloring of g, False otherwise.
    """
    nodes = set(g.keys())

    # Check all subsets of nodes of size 0 to |V| as red set
    for i in range(len(g)+1):
        for red in itertools.combinations(nodes, i):
            red = set(red)

            # Ensure that there are no edges among nodes in red set
            if not has_internal_edge(g, red):
                # Check all subsets of nodes of size 0 to |V|-|red| as green set
                for j in range(len(g)-i+1):
                    for green in itertools.combinations(nodes - red, j):
                        green = set(green)

                        # Ensure that there are no edges among nodes in green set
                        if not has_internal_edge(g, green):
                            # blue set is the remainder of nodes in the graph
                            blue = nodes - red - green

                            # Ensure that there are no edges among nodes in blue set
                            if not has_internal_edge(g, blue):
                                # sets red, green, blue are a three coloring
                                return True

    # There is no three coloring
    return False

def run_example():
    """
    Compute some examples
    """
    print "GRAPH1 is 3 colorable =", is_three_colorable(GRAPH1)
    print "GRAPH2 is 3 colorable =", is_three_colorable(GRAPH2)
    print "GRAPH3 is 3 colorable =", is_three_colorable(GRAPH3)
    print "GRAPH4 is 3 colorable =", is_three_colorable(GRAPH4)
    
run_example()

