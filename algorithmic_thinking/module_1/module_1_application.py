'''
    Application portion of Module 1


'''


#import codeskulptor
#codeskulptor.set_timeout(20)

# general imports
import urllib2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab




def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


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


def normalise_indegrees(indegrees):
    '''
    normalize the distribution (make the values in the dictionary sum to one)
    returns a dictionary of normalised values
    '''
    #first need to get total value
    total = 0
    count = 0
    for node in indegrees.keys():
        total += indegrees[node]
        count += 1
    print 'num of nodes:', count, 'total value =', total

    #now build an updated dictionary
    result = {}
    for node in indegrees.keys():
        result[node] = float(indegrees[node]) / total
        #print 'node', node, 'value =', indegrees[node]
    return result
  

def plot_points(normalised):
    '''
    plots graph of points in normalised
    '''
    num_bins = len(normalised)
    print 'plotting', num_bins, 'points'

    Dictionary_Length = len(normalised)
    Max_Key_Length = 15
    Sorted_Dict_Values = sorted(normalised.values(), reverse=True)
    Sorted_Dict_Keys = sorted(normalised, key=normalised.get, reverse=True)
    for i in range(0,Dictionary_Length):
        Key = Sorted_Dict_Keys[i]
        #Key = Key[:Max_Key_Length]
        Sorted_Dict_Keys[i] = Key
    X = np.arange(Dictionary_Length)
    Colors = ('b','g','r','c')  # blue, green, red, cyan

    Figure = plt.figure()
    Axis = Figure.add_subplot(1,1,1)
    for i in range(0,Dictionary_Length):
        Axis.bar(X[i], Sorted_Dict_Values[i], align='center',width=0.5, color=Colors[i%len(Colors)])

    Axis.set_xticks(X)
    xtickNames = Axis.set_xticklabels(Sorted_Dict_Keys)
    plt.setp(Sorted_Dict_Keys)
    plt.xticks(rotation=20)
    ymax = max(Sorted_Dict_Values) + 1
    plt.ylim(0,ymax)

    plt.show()

    

trial = {9306094: 0.504172714078374e-06, 9306095: 0.13388969521045e-05, 9306096: 9.354589985486212e-05, 9306097: 8.504172714078374e-06, 9306098: 1.9843069666182873e-05, 9306099: 2.834724238026125e-06, 9306100: 8.504172714078374e-06, 9306101: 3.118196661828737e-05, 9306102: 3.118196661828737e-05, 9306103: 2.2677793904209e-05, 9306104: 5.66944847605225e-06, 9306105: 0.0, 9306106: 2.5512518142235124e-05, 9306107: 3.118196661828737e-05, 9306109: 0.0, 9306110: 8.504172714078374e-06, 9306111: 2.2677793904209e-05}



plot_points(trial)





def in_degree_distribution():
    '''
    Question 1:
    in-degree distribution for citation graph. Once you have computed this 
    distribution, normalize the distribution (make the values in the dictionary
    sum to one) and then compute a log/log plot of the points in this normalized
    distribution. How you create this point plot is up to you. You are welcome
    to use a package such as matplotlib for desktop Python, use the simpleplot
    module in CodeSkulptor, or use any other method that you wish. 
    This class page on "Creating, formatting, and comparing plots" gives an
    overview of some of the options that we recommend for creating plots.
    '''
    #load the graph
    citation_graph = load_graph(CITATION_URL)
    #for paper in citation_graph:
    #    print paper.items()
    #print citation_graph.items()

    indegrees =  compute_in_degrees(citation_graph)
    #print 'indegree =', compute_in_degrees(citation_graph)


    normalised = normalise_indegrees(indegrees)
    print normalised






in_degree_distribution()








