''' how to generate a number with probability p'''
import random
p = 0.4

count = 0
for i in range(1000000):
    if random.random() <= p:
        #print True
        count += 1
    else:
        #print False
        pass

print count/1000000.0

class Foo(object):
    pass

o = Foo()
print o
a = Foo
print a

class Foo(object):
    pass

print [Foo() for i in xrange(4)]

import pylab

l = pylab.array([1, 2, 3])
m = pylab.array([10, 20, 30])
print l, m
k = (l+m)/2.0
print k
print k[2]

d = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4}


if d['be'] == 3:
    print d.get('a',0)