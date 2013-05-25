from ps10 import *

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)
    
class WeightedEdge(Edge):
    def __init__(self, src, dest, tot_dist, out_dist):
        Edge.__init__(self, src, dest)
        self.total_distance = tot_dist
        self.outdoor_distance = out_dist
    
    def getTotalDistance(self):
        return self.total_distance
    
    def getOutdoorDistance(self):
        return self.outdoor_distance
     
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.getSource(), self.getDestination(), self.getTotalDistance(), self.getOutdoorDistance())

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]
    
class WeightedDigraph(Digraph):
    
    def addEdge(self, edge):
        assert type(edge) == WeightedEdge
        src = edge.getSource()
        dest = edge.getDestination()
        tot_dist = float(edge.getTotalDistance())
        out_dist = float(edge.getOutdoorDistance())
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        else:
            # {src:[[dest1, (w11, w12)],[[dest2, (w21, w22)],...]}
            self.edges[src].append([dest, (tot_dist, out_dist)])
            
    def childrenOf(self, node):
        assert type(node) == Node
        #return the 1st element of all sublists in self.edges
        return [child[0] for child in self.edges[node]]
    
    def __str__(self):
        # b->c (3.0, 1.0)
        strings = []
        for src in self.edges: #return a list of keys (sources)
            for dest in self.edges[src]: # return all destinations for each of the sources
        #         print src, dest
                strings.append('{0}->{1} ({2}, {3})'.format(src, dest[0], dest[1][0], dest[1][1]))
        return '\n'.join(strings)


g = WeightedDigraph()

g.addNode(Node('1'))
g.addNode(Node('2'))
g.addNode(Node('3'))
g.addNode(Node('4'))

g.addEdge(WeightedEdge(Node('1'), Node('2'), 10.0, 5.0))
g.addEdge(WeightedEdge(Node('1'), Node('4'), 5.0, 1.0))
g.addEdge(WeightedEdge(Node('2'), Node('3'), 8.0, 5.0))
g.addEdge(WeightedEdge(Node('4'), Node('3'), 8.0, 5.0))

print g
print 'nodes = ',g.nodes
print 'edges = ',g.edges

# helper function
def opt_all_DFS(graph, start, end, maxTotalDist, maxDistOutdoors, path=[]):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
#     print 'Current dfs path:', printPath(path)
#     print '01. path = '+str(path)+' len tot = '+str(path_total_distance(graph, path))+' len out = '+str(path_outdoor_distance(graph, path)) #TP01
    if start == end:         
        return [path]
#         return path
    paths = [] # initialize list of all possible paths
    for node in graph.childrenOf(start):
        #~~~~~~~~~~~~~ optimization ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#         print '----OPTIMISATION path = '+str(path)+' len tot = '+str(path_total_distance(graph, path))+' len out = '+str(path_outdoor_distance(graph, path)) #TP01
        if path_total_distance(graph, path+[node]) > float(maxTotalDist) or \
            path_outdoor_distance(graph,path+[node]) > float(maxDistOutdoors): # if maxTotalDist is reached so far
            continue # continue with the next node
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
        if node not in path:
            # recursive case: the first node of children nodes becomes the start node each time
            new_path = opt_all_DFS(graph, node, end, maxTotalDist, maxDistOutdoors, path)
#             print '============= 02. new_path = '+str(new_path)
#             paths.append(new_path)
#             if len(new_path)
            for p in new_path: # in order to flatten newpath list []
#                 print '-----------------%f %f'%(path_total_distance(graph, p),float(maxTotalDist))
#                 print '-----------------%f %f'%(path_outdoor_distance(graph, p),float(maxDistOutdoors))
                paths.append(p)
    # now return from recursive case when all nodes in graph.childrenOf(start) have been examined
#     print ' @@@@@@@@@@@@@@ 03. paths = ',paths #TP03
    return paths

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
    #Find ALL possible paths from start to end w/ constrains of maxTotalDist and, maxDistOutdoors
    start = Node(start)
    end = Node(end)
    all_paths = opt_all_DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, path=[])
#     print 'ALL PATHS = ',all_paths
    if len(all_paths) == 0: raise ValueError
    
    best_path = None # initialize the best path found so far
    best_dist = maxTotalDist # initialize the shortest distance so far as the max allowed dist
    for path in all_paths:
#         print 'PATH = ',path
        tot_dist = path_total_distance(digraph, path)
        if tot_dist <= best_dist:
            # update the shortest distance and best path found so far
            best_dist = tot_dist
            best_path = path
 
    return [n.getName() for n in best_path] # representation of nodes as building numbers <strings>

directedDFS(g, '1', '3', 10, 10)
