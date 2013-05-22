# set
l = [1, 2, 3, 2]

print l
print set(l)

#__hash__
class Node(object):
    def __init__(self, name):
        self.name = str(name)

#     def __eq__(self, other):
#         return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

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