import copy
a = {1:[1, 2, 3], 2:[4, 5, 6], 3:'abc'}
print a
print a[1]

b = a[1]
print b

a[1].append(666)
print a
print b

print 'copy the contents of a[1]'

a = {1:[1, 2, 3], 2:[4, 5, 6], 3:'abc'}
print a
print a[1]

c = a[1][:]
print c

a[1].append(777)
print a
print c

print 'swallow copy dict a'

a = {1:[1, 2, 3], 2:[4, 5, 6], 3:'abc'}
print a
print a[1]

c = a.copy()
print c

a[1].append(777)
print 'a =',a
print 'c =',c

print 'deep copy dict a'

a = {1:[1, 2, 3], 2:[4, 5, 6], 3:'abc'}
print a
print a[1]

c = copy.deepcopy(a)
print c

a[1].append(777)
print 'a =',a
print 'c =',c