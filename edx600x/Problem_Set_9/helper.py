import random, pylab

x = [random.random() for i in xrange(100)]
y = [2*random.random() for i in xrange(100)]

# subplot sharing the same axis (http://matplotlib.org/examples/pylab_examples/subplots_demo.html)
f, axarr = pylab.subplots(2, sharex=True)

print f
print axarr
# create an empty figure 1
pylab.figure(1)
# inside that figure 1 draw 2 subplots, one plot and one hist
axarr[0].plot(x, y , 'bo')
axarr[1].hist(y, bins=100)

#subplot not share the same axis (http://matplotlib.org/examples/pylab_examples/subplot_demo.html)
# create a second empty figure 2
pylab.figure(2)
# inside that figure 1 draw 2 subplots, one plot 211 and one hist 212
pylab.subplot(211)
pylab.plot(x, y, 'bo')
pylab.subplot(212)
pylab.hist(y, bins=100)
# finally show all previously created figures 1 and 2
#pylab.show()

# how many bins for hist?
pylab.figure("how many bins?")
pylab.hist(x, bins=10)
pylab.show()