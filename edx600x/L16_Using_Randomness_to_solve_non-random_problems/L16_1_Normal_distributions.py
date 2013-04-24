import random, pylab

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5



def makeNormal(mean, sd, numSamples):
    samples = []
    for i in range(numSamples):
        samples.append(random.gauss(mean, sd))
    pylab.hist(samples, bins = 101)

makeNormal(0, 1.0, 100000)
pylab.show()





