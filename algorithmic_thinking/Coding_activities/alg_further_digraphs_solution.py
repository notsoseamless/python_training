"""
Solution to "Directed graphs" from Further activities
"""

# Exercise 1 - Digraph

{0: set([1]), 1: set([2]), 2: set([3]), 3: set([4]), 4: set([5]), 5: set([0])}

# Exercise 2 - In-Degree

def in_degree(digraph, node):
    """
    Computes the in-degree of the given node.

    Arguments:
    digraph -- a dictionary representation of a digraph.
    node    -- the given to node.

    Returns:
    The in-degree of node.
    """
    count = 0

    for key in digraph.keys():
        for to_node in digraph[key]:
            if to_node == node:
                count = count + 1

    return count

