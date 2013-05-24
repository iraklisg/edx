from L19_2_Graph_Implementation import *

# Create GRAPH 
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

#################

def DFS(graph, start, end, path = []):
    """
    Depth-First Search algorithm

    parameters: graph: instance of WeightedGraph class
                start, end: instances of Node class
    Assumes that start+end Nodes are in the graph

    yields: lists (representing all possible paths from start to end)
    """
    path = path + [start]
    #print 'Current DFS path:', path
    if start == end:
        yield path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph, node, end, path)
            for nPath in newPath:
                yield nPath
                
                
all_paths = DFS(g, nodes[0], nodes[5], path = [])
print all_paths
for path in all_paths:
    print path