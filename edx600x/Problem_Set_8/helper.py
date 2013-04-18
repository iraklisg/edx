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