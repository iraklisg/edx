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

def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
#     print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
#         print node
        if node not in path: #avoid cycles
            # recursive case: the first node of children nodes becomes the start node each time
            newPath = DFS(graph,node,end,path,shortest) 
#             print newPath
            if newPath != None:
                return newPath

def find_all_paths_original(graph, start, end, path=[]):
    path = path + [start]
#     print 'Current dfs path:', printPath(path)
    if start == end:
#         print path           
        return [path]
    paths = []
    for node in graph.childrenOf(start):
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_all_paths(graph, start, end, path=[]):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
#     print 'Current dfs path:', printPath(path)
    print '01. path = ',path #TP01
    if start == end:         
        return path
    paths = [] # initialize list of all possible paths
    for node in graph.childrenOf(start):
        if node not in path:
            # recursive case: the first node of children nodes becomes the start node each time
            new_path = find_all_paths(graph, node, end, path)
            print '02. new_path = ',new_path #TP02
            paths.append(new_path)
#             for i in new_path: # in order to flatten newpath list []
#                 paths.append(i)
    # now return from recursive case when all nodes in graph.childrenOf(start) have been examined
    print '03. paths = ',paths #TP03
    return paths

#########################

# path = DFS(g, nodes[0], nodes[5], path = [], shortest = None)
# print path
# print printPath(path)
    
all_paths = find_all_paths(g, nodes[0], nodes[5], path = [])
for path in all_paths:
    print printPath(path)

##########################

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