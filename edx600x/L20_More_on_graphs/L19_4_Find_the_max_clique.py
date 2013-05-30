class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
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
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)




# given a graph create all possible powersets from grph's node and return all possible collections of nodes
def powerGraph(gr):
    nodes = gr.nodes
    nodesList = []
    for elt in nodes:
        nodesList.append(elt)
    pSet = powerSet(nodesList)
    return pSet # here I have all possible different subgraphs from graph

def powerSet(elts):
    if len(elts) == 0:
        return [[]] # power set of all elements of length 0
    else:
        smaller = powerSet(elts[1:]) # take all the elements except the first one
        elt = [elts[0]] #take the first element
        withElt = []
        for s in smaller:
            withElt.append(s + elt) # for all n-1 elements  add the 1st element
        allofthem = smaller + withElt # combine the two sets
        return allofthem

def maxClique(gr):
    candidates = powerGraph(gr) # calculate a possible subgraphs of graph
    keepEm = []
    for candidate in candidates:
        if allConnected(gr, candidate):
            keepEm.append(candidate)
    bestLength = 0
    bestSoln = None
    for test in keepEm:
        if len(test) > bestLength:
            bestLength = len(test)
            bestSoln = test
    return bestSoln

def allConnected(gr,candidate):
    for n in candidate: # for every element in that subgraph
        for m in candidate: # for every other element of that subgraph
            if not n == m:
                if n not in gr.childrenOf(m): # check if all the other elements are children of the initial element
                    return False
    return True


def testGraph():
    nodes = []
    for name in range(5):
        nodes.append(Node(str(name)))
    g = Graph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[0]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[4],nodes[3]))
    return g


trialGraph = testGraph()
myClique = maxClique(trialGraph)




        

