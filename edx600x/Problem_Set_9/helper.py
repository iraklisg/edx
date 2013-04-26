import random, pylab

x = [random.random() for i in xrange(1000)]
y = [2*random.random() for i in xrange(1000)]

# subplot sharing the same axis (http://matplotlib.org/examples/pylab_examples/subplots_demo.html)
f, axarr = pylab.subplots(2, sharex=True)

print f
print axarr

axarr[0].plot(x, y , 'bo')
axarr[1].hist(y, bins=100)
pylab.show()

#subplot not share the same axis (http://matplotlib.org/examples/pylab_examples/subplot_demo.html)
pylab.subplot(211)
pylab.plot(x, y)
pylab.subplot(212)
pylab.hist(y, bins=100)
pylab.show()