import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # Your code here
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    # for each rabbit in the current rabbit population CURRENTRABBITPOP
    for i in xrange(CURRENTRABBITPOP):
        p_rabit_reproduction = 1.0 - (CURRENTRABBITPOP / float(MAXRABBITPOP))
        if random.random() <= p_rabit_reproduction and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # Your code here
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    global CURRENTFOXPOP
    # for each fox currently in the forest CURRENTFOXPOP
    for i in xrange(CURRENTFOXPOP):
        p_fox_eats_rabbit = CURRENTRABBITPOP / float(MAXRABBITPOP)
        if random.random() <= p_fox_eats_rabbit and CURRENTRABBITPOP > 10: # is fox succeed in hunting and there are more than 10 rabbits
            CURRENTRABBITPOP -= 1 # the fox eats on rabbit
            if random.random() <= 1/3.0: # with probability 1/3
                CURRENTFOXPOP += 1 # gives birth to a new little fox
        else: # if the fox does not succeed in hunting
            if random.random() <= 9/10.0 and CURRENTFOXPOP > 10: # with probability 1/10, she dies given that there always are at least 10 foxes in the forest
                CURRENTFOXPOP -=1 # poor fox
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    # Your code here
    rabbit_populations = []
    fox_populations = []
    for i in xrange(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)
        
(r, f) = runSimulation(200)
pylab.figure(1)
pylab.plot(r, 'b.')
pylab.plot(f, 'r.')
#coeff = pylab.polyfit(range(len(r)), r, 2)
#trend = pylab.polyval(coeff, range(len(r)))
x_vals = pylab.array(range(len(r)))
a, b, c = pylab.polyfit(x_vals, r, 2)
est_yvals = a*x_vals**2 + b*x_vals + c
pylab.plot(est_yvals, 'b-')

pylab.show()