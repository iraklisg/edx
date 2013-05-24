from L19_2_Graph_Implementation import *

def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        print path
        return path
    for node in graph.childrenOf(start):
        print node
        if node not in path: #avoid cycles
            # recursive case: the first node of children nodes becomes the start node each time
            newPath = DFS(graph,node,end,path,shortest) 
            if newPath != None:
                return newPath

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        print path           
        return [path]
    paths = []
    for node in graph.childrenOf(start):
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

################
nodes = []
# Create all nodes and add them to the list above
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]
# add nodes to the graph
g = Graph()
for n in nodes:
    g.addNode(n)
g.addEdge(Edge(nodes[0],nodes[1]))
g.addEdge(Edge(nodes[0],nodes[2]))
g.addEdge(Edge(nodes[1],nodes[4]))
g.addEdge(Edge(nodes[2],nodes[3]))
g.addEdge(Edge(nodes[3],nodes[5]))
g.addEdge(Edge(nodes[4],nodes[5]))

DFS(g, nodes[0], nodes[5], path = [], shortest = None)
l = find_all_paths(g, nodes[0], nodes[5], path = [])
printPath(l) 

def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = DFS(g, nodes[0], nodes[5])
    print 'Shortest path found by DFS:', printPath(sp)