# 6.00x Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

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


# g = WeightedDigraph()
# na = Node('a')
# nb = Node('b')
# nc = Node('c')
# g.addNode(na)
# g.addNode(nb)
# g.addNode(nc)
# e1 = WeightedEdge(na, nb, 15, 10)
# print e1
# print e1.getTotalDistance()
# print e1.getOutdoorDistance()
# e2 = WeightedEdge(na, nc, 14, 6)
# e3 = WeightedEdge(nb, nc, 3, 1)
# print e2
# print e3
# g.addEdge(e1)
# g.addEdge(e2)
# g.addEdge(e3)
# print '#######'
# print g
