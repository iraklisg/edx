# 6.00x Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    f = open(mapFilename, 'r')
    # f.readline() reads a single line from the file; a newline character (\n) is
    # left at the end of the string, and is only omitted on the last line of the
    # file if the file doesn't end in a newline. This makes the return value unambiguous
    # if f.readline() returns an empty string, the end of the file has been reached,
    # while a blank line is represented by '\n', a string containing only a single newline.
    
    # Initialize a weighted digraph
    g = WeightedDigraph()
    all_data = []
    # READ ALL DATA FROM FILE
    # create a list of all data [[src, dest, w1, w2],[src, dest, w1, w2],[src, dest, w1, w2], ...]
    # ADD NODES (src and dest) in graph, if they do not exist already
    line = None # initialize line
    while True:
        line = f.readline()
        if line == '': #until the end of the file is reached, i.e. until line is an empty string
            break
        data = string.split(line)
        all_data.append(data)
        # if both src and dest nodes do not exist in graph yet (otherwise it raises an error)
        # ADD NODE
        if not g.hasNode(Node(data[0])):
            g.addNode(Node(data[0])) # add source node
        if not g.hasNode(Node(data[1])):
            g.addNode(Node(data[1])) # add destination node
    f.close() # close the file since all data is stored in all_data list variable
    # For every sublist in all_data that contains info for an edge
    # ADD EDGE and the corresponding info to graph
    for edge in all_data:
        g.addEdge(WeightedEdge(Node(edge[0]),Node(edge[1]),float(edge[2]),float(edge[3])))
    return g
        

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

# helper function - calculate path_tot_distance
def path_total_distance(graph, path):
    clone_path = path[:] # clone path list
    tot_dist = 0
    for src_node in path[:-1]: # access every node in path except last one (current src node in path)
#         print 'currently accessed src_node = ', src_node
        clone_path = clone_path[1:] # path list shifted right to access next node in path
#         print 'clone path = ', clone_path
        next_node = clone_path[0] # access next node in path (current dest node in path)
#         print 'next node in path = ',next_node
        possible_destinations = graph.edges[src_node] # find the list of all possible destinations from src_node
        for i in xrange(len(possible_destinations)): # for every possible destination from src_node
#             print 'currently accessed dest_node = ', possible_destinations[i]
            if possible_destinations[i][0] == next_node: # if possible destination is the next node in path
                tot_dist += graph.edges[src_node][i][1][0] # find total distance and update
                break
    return tot_dist

# helper function - calculate path_outdoor_distance
def path_outdoor_distance(graph, path):
    clone_path = path[:] # clone path list
    tot_dist = 0
    for src_node in path[:-1]: # access every node in path except last one (current src node in path)
#         print 'currently accessed src_node = ', src_node
        clone_path = clone_path[1:] # path list shifted right to access next node in path
#         print 'clone path = ', clone_path
        next_node = clone_path[0] # access next node in path (current dest node in path)
#         print 'next node in path = ',next_node
        possible_destinations = graph.edges[src_node] # find the list of all possible destinations from src_node
        for i in xrange(len(possible_destinations)): # for every possible destination from src_node
#             print 'currently accessed dest_node = ', possible_destinations[i]
            if possible_destinations[i][0] == next_node: # if possible destination is the next node in path
                tot_dist += graph.edges[src_node][i][1][1] # find total distance and update
                break
    return tot_dist

# helper function
def all_DFS(graph, start, end, path=[]):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
#     print 'Current dfs path:', printPath(path)
#     print '01. path = ',path #TP01
    if start == end:         
        return [path]
#         return path
    paths = [] # initialize list of all possible paths
    for node in graph.childrenOf(start):
        if node not in path:
            # recursive case: the first node of children nodes becomes the start node each time
            new_path = all_DFS(graph, node, end, path)
#             print '02. new_path = ',new_path #TP02
#             paths.append(new_path)
#             if len(new_path)
            for i in new_path: # in order to flatten newpath list []
                paths.append(i)
    # now return from recursive case when all nodes in graph.childrenOf(start) have been examined
#     print '03. paths = ',paths #TP03
    return paths

# helper function
def mod_all_DFS(graph, start, end, maxTotalDist, maxDistOutdoors, path=[]):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
#     print 'Current dfs path:', printPath(path)
#     print '01. path = ',path #TP01
    if start == end:         
        return [path]
#         return path
    paths = [] # initialize list of all possible paths
    for node in graph.childrenOf(start):
        if node not in path:
            # recursive case: the first node of children nodes becomes the start node each time
            new_path = mod_all_DFS(graph, node, end, maxTotalDist, maxDistOutdoors, path)
#             print '02. new_path = ',new_path #TP02
#             paths.append(new_path)
#             if len(new_path)
            for p in new_path: # in order to flatten newpath list []
#                 print '-----------------%f %f'%(path_total_distance(graph, p),float(maxTotalDist))
#                 print '-----------------%f %f'%(path_outdoor_distance(graph, p),float(maxDistOutdoors))
                if path_total_distance(graph, p) <= float(maxTotalDist) and \
                path_outdoor_distance(graph,p) <= float(maxDistOutdoors):
                    paths.append(p)
    # now return from recursive case when all nodes in graph.childrenOf(start) have been examined
#     print '03. paths = ',paths #TP03
    return paths

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance traveled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    #consider first finding all valid paths that satisfy the max distance outdoors constraint,
    #and then going through those paths and returning the shortest, rather than trying to
    #fulfill both constraints at once.
    
    #Find ALL possible paths from start to end w/ constrains of maxTotalDist and, maxDistOutdoors
    start = Node(start)
    end = Node(end)
    all_paths = mod_all_DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, path=[])
    if len(all_paths) == 0: raise ValueError
    
    best_path = None # initialize the best path found so far
    best_dist = maxTotalDist # initialize the shortest distance so far as the max allowed dist
    for path in all_paths:
        tot_dist = path_total_distance(digraph, path)
        if tot_dist <= best_dist:
            # update the shortest distance and best path found so far
            best_dist = tot_dist
            best_path = path
        
    return [n.getName() for n in best_path] # representation of nodes as building numbers <strings>
    

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass


mitMap = load_map("test_mit_map.txt")
# print mitMap

# all_paths = all_DFS(mitMap, Node('68'), Node('36'))
# all_paths = mod_all_DFS(mitMap, Node('68'), Node('36'), 179, 80)
# print all_paths
# for path in all_paths:
#      print path_total_distance(mitMap, path)
#      print path_outdoor_distance(mitMap, path)

# print bruteForceSearch(mitMap, Node('68'), Node('36'), 180, 41)

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    #Test cases
    mitMap = load_map("mit_map.txt")
    print mitMap
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

#     Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
