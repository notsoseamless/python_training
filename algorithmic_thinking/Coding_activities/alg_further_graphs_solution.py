"""
Solutions for "Undirected graphs" in Further activities
"""

#Exercise 1 - Node Count
def node_count(graph):
    """
    Returns the number of nodes in a graph.

    Arguments:
    graph -- The given graph.

    Returns:
    The number of nodes in the given graph.
    """
    return len(graph.keys())

#Exercise 2 - Edge Count

def edge_count(graph):
    """
    Returns the number of edges in a graph.

    Arguments:
    graph -- The given graph.

    Returns:
    The number of edges in the given graph.
    """
    edge_double_count = 0
    for nodeKey in graph.keys():
        edge_double_count = edge_double_count + len(graph[nodeKey])

    return edge_double_count / 2

