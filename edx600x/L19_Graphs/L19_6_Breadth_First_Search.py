from L19_2_Graph_Implementation import *

def BFS(graph, start, end, q = []):
    initPath = [start] # initial path is just the start node
    q.append(initPath) # put at the end of queue `q` (append) the init path
    while len(q) != 0: # if there are still items in queue
        tmpPath = q.pop(0) # pop out the first element (element 0) in queue
        lastNode = tmpPath[len(tmpPath) - 1] # get the last node in queue
        print 'Current dequeued path:', printPath(tmpPath)
        if lastNode == end: # if that last node is the goal node I'm done...
            return tmpPath # ...and return the path
        for linkNode in graph.childrenOf(lastNode): # if not, I take all the children of that last node
            if linkNode not in tmpPath: # for each of these children that are not in the path already 
                newPath = tmpPath + [linkNode] # I create a new path by appending the child node...
                q.append(newPath) # ...and append this new path
    return None