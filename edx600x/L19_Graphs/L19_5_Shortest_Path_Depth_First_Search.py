from L19_2_Graph_Implementation import *

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start] # concatenate lists of Node objects
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path)
                if newPath != None:
                    shortest = newPath
    return shortest

L1 = []
L2 = [2, 3]

print L1 + L2
print L2 + L1