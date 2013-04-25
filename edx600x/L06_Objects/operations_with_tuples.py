'''tuples'''
t1 = (1, 2, 3)
print t1
print type(t1)
x, y, z = t1
print x, y, z
print type(x)

'''lists'''
L1 = [1, 2, 'abc']
k, l, m = L1
print k, l, m
print type(k)
print type(m)

'''dictionaries'''
d1 = {'a':1, 'b':2, 88:3}
i, j, k = d1
print d1
print i, j, k # returns keys in random order!!!
print type(i)
print type(j)

i, j, k = d1.keys()
print d1
print i, j, k # returns keys in random order!!!
print type(i)
print type(j)

i, j, k = d1.values()
print d1
print i, j, k # returns values in random order!!!
print type(i)
print type(j)

i, j, k = d1.items()
print d1
print i, j, k # returns pair of keys:values as tuples in random order!!!

print type(i)
print type(j)