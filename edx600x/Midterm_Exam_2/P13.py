import random
import pylab
res = []
for i in xrange(1000):
    res.append(random.gauss( 50,10) + random.gauss( 70, 10 ))

pylab.hist(res, bins=100)
pylab.show()