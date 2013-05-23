# set
l = [1, 2, 3, 2]

print l
print set(l)

#__hash__
class Node(object):
    def __init__(self, name):
        self.name = str(name)

    def __eq__(self, other):
        return self.name == other.name

#     def __hash__(self):
#         return self.name.__hash__()



a = Node(1)
print '12 a =', a.name
print '13', a.__hash__()

b = Node(1)
print '16 b =', b.name
print '17', b.__hash__()

print '19', a == b #watch it in 5)
print '20', a in [b]
print '21', a in set([b]) #watch it in 3)
print '22', a in {b:[]}

print '24', a.name == b.name
print '25', a.name in [b.name]
print '26', a.name in set([b.name])
print '27', a.name in {b.name:[]}

# 1) run this code
# 2) uncomment __hash__ method and run the code
# 3) you will see difference
# 4) comment out __eq__ method and run the code
# 5) you will see difference 

## difference between type() and isinstance() 
class bNode(Node):
    pass
c = bNode('b')
print type(a) == type(b)
print type(c) == Node
print type(c) == bNode
print isinstance(c, Node)

## 
print "-------------------------------------------"
d = {'a':[['b', (1,2)], ['c', (3,4)]], 'd':[['c', (66,77)]]}

for src in d: #return a list of keys (sources)
    for dest in d[str(src)]: # return all destinations for each of the sources
#         print src, dest
        print '%s->%s (%.2f, %.2f)'%(src, dest[0], dest[1][0], dest[1][1])
    
    
# read from file
print '~~~~~~~~~~ Read from file ~~~~~~~~~~~'
import string # split()
from graph import * 
f = open('test_mit_map.txt', 'r')
# f.readline() reads a single line from the file; a newline character (\n) is
# left at the end of the string, and is only omitted on the last line of the
# file if the file doesn't end in a newline. This makes the return value unambiguous
# if f.readline() returns an empty string, the end of the file has been reached,
# while a blank line is represented by '\n', a string containing only a single newline.

# Initialize a weighted digraph
g = WeightedDigraph()
all_data = []
line = None # initialize line
# print line
while True:
    line = f.readline()
    if line == '': #until the end of the file is reached, i.e. until line is an empty string
        break
    data = string.split(line)
    all_data.append(data)
#     print line
#     print data
    if g.hasNode(Node(data[0])):
        print str(data[0])+'Existed'
    else:
        g.addNode(Node(data[0]))
print g.nodes
print all_data

for edge in all_data:
    print edge
    g.addEdge(WeightedEdge(Node(edge[0]),Node(edge[1]),float(edge[2]),float(edge[3])))
print g.edges
print g
    


















    