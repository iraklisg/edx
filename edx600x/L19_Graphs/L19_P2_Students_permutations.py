from L19_2_Graph_Implementation import *

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
    
# create the appropriate edges under the condition
# edges connect two permutations if one can be made into the other by swapping two adjacent students
# then add the edges to the graph

# Graph.addEge(edge)
# edge = Edge(src, dest)
g.addEdge(Edge(nodes[0],nodes[1]))
g.addEdge(Edge(nodes[0],nodes[2]))
g.addEdge(Edge(nodes[1],nodes[4]))
g.addEdge(Edge(nodes[2],nodes[3]))
g.addEdge(Edge(nodes[3],nodes[5]))
g.addEdge(Edge(nodes[4],nodes[5]))