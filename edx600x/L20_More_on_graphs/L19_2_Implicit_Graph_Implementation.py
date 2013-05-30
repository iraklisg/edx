class puzzle(object):
    def __init__(self, order): # order = an initial layout of the puzzle
        self.label = order # label is the current layout of the puzzle 
        for index in range(9):
            if order[index] == '0':
                self.spot = index # spot = the position of empty tile
                return None
    def transition(self, to): # a location; the place to witch I'm going to do a shift
        label = self.label
        blankLocation = self.spot # where the blank was
        newBlankLabel = str(label[to]) # is the number of tile i'm now shifting
        newLabel = ''
        for i in range(9):
            if i == to: # the index is 
                newLabel += '0'
            elif i == blankLocation: # the location the blank was i now the location of the tile I'm shifting
                newLabel += newBlankLabel
            else:
                newLabel += str(label[i]) # keep the other tiles n the same place
        return puzzle(newLabel)
    def __str__(self):
        return self.label



def DFSWithGeneratorShortest(start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    if start.label == end.label:
        return path
    for shift in shiftDict[start.spot]:
        new = start.transition(shift)
        if new.label not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFSWithGeneratorShortest(new,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFSWithGenerator(start, end, q = []):
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if notInPath(new, tmpPath):
                newPath = tmpPath + [new]
                q.append(newPath)
    return None

def DFSWithGenerator(start, end, stack = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    initPath = [start]
    stack.insert(0, initPath) # @ I'm inserting instead of appending
    while len(stack)!= 0:
        tmpPath = stack.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]: # go to last node (state) and go to the place where the blank is
            new = lastNode.transition(shift) # for each of the places the new blank could be, i compute using that transition function the new state of the system (i.e. compute the next new nodes))
            if notInPath(new, tmpPath): #avoid cycles
                newPath = tmpPath + [new] # append the new nodes in path
                stack.insert(0, newPath)  # @ I'm inserting instead of appending
    return None


def notInPath(node, path):
    for elt in path:
        if node.label == elt.label:
            return False
    return True


shiftDict = {}
shiftDict[0] = [1, 3]
shiftDict[1] = [0, 2, 4]
shiftDict[2] = [1, 5]
shiftDict[3] = [0, 4, 6]
shiftDict[4] = [1, 3, 5, 7]
shiftDict[5] = [2, 4, 8]
shiftDict[6] = [3, 7]
shiftDict[7] = [4, 6, 8]
shiftDict[8] = [5, 7]

goal = puzzle('012345678')
test1 = puzzle('125638047')


def printGrid(pzl):
    data = pzl.label
    print data[0], data[1], data[2]
    print data[3], data[4], data[5]
    print data[6], data[7], data[8]
    print ''

def printSolution(path):
    for elt in path:
        printGrid(elt)

path = BFSWithGenerator(test1, goal)
print printSolution(path)


