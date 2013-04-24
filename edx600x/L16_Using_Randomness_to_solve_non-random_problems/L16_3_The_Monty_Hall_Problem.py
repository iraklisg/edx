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
#set font size for text
pylab.rcParams['legend.fontsize'] = 20



def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3

def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2,3])
    if guessDoor == 2:
        return random.choice([1,3])
    return random.choice([1,2])
    
def simMontyHall(numTrials, chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    prizeDoorChoices = [1,2,3]
    guessChoices = [1,2,3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)

def displayMHSim(simResults, title):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

simResults = simMontyHall(100000, montyChoose)
displayMHSim(simResults, 'Monty Chooses a Door')
pylab.figure()
simResults = simMontyHall(100000, randomChoose)
displayMHSim(simResults, 'Door Chosen at Random')
pylab.show()



def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    estimates = []
    for Needles in xrange(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 2*(inCircle/float(Needles))

def estPi(precision = 0.01, numTrials = 20):
    numNeedles = 1000
#    numTrials = 20
    sDev = precision
    while sDev >= (precision/4.0):
        estimates = []
        for t in range(numTrials):
            piGuess = throwNeedles(numNeedles)
            estimates.append(piGuess)
        sDev = stdDev(estimates)
        curEst = sum(estimates)/len(estimates) 
        curEst = sum(estimates)/len(estimates)
        print 'Est. = ' + str(curEst) +\
              ', Std. dev. = ' + str(sDev)\
              + ', Needles = ' + str(numNeedles)
        numNeedles *= 2
    return curEst

##estPi()

def integrate(a, b, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        pinSum += f(random.uniform(a, b))
    average = pinSum/numPins
    return average*(b - a)

def one(x):
    return 1.0

##print integrate(0, 8, one, 100000)
##4 + 3
##import math
##print integrate(0, 8, math.sin, 1000000)

def doubleIntegrate(a, b, c, d, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        pinSum += f(x, y)
    average = pinSum/numPins
    return average*(b - a)*(d - c)

def f(x, y):
    return 4 - x**2 - y**2

##print doubleIntegrate(0, 1.25, 0, 1.25, f, 100000)