"""
Solution for "Finding popular nodes" in Further activities
"""

import alg_load_graph

# Increase timeout for 10000 node graph in CodeSkulptor
#import codeskulptor
#codeskulptor.set_timeout(20)

GRAPH10_URL = "http://storage.googleapis.com/codeskulptor-alg/random10.txt"
GRAPH100_URL = "http://storage.googleapis.com/codeskulptor-alg/random100.txt"
GRAPH1000_URL = "http://storage.googleapis.com/codeskulptor-alg/random1000.txt"
GRAPH10000_URL = "http://storage.googleapis.com/codeskulptor-alg/random10000.txt"


def node_count(graph):
    """
    Returns the number of nodes in a graph.

    Arguments:
    graph -- The given graph.

    Returns:
    The number of nodes in the given graph.
    """
    return len(graph.keys())


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


def find_popular_nodes(graph):
    """
    Find the set of all nodes in graph whose degree is higher than the
    average degree in graph.

    Arguments:
    graph - an undirected graph

    Returns:
    Set of popular nodes in graph
    """
    popular = set()
    avgdeg = 2 * edge_count(graph) / node_count(graph)
    for node in graph:
        nodedeg = len(graph[node])
        if nodedeg > avgdeg:
            popular.add(node)
    return popular

def run_example():
    """
    Computing the popular nodes for an example graph
    """
    my_graph = alg_load_graph.load_graph(GRAPH100_URL)
    print "There are", len(find_popular_nodes(my_graph)), "popular nodes"
    
run_example()

