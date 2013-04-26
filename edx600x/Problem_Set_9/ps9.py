# 6.00 Problem Set 9

import numpy
import random
import pylab
#from ps8b import *
from ps8b_precompiled_27 import *

#
# PROBLEM 1
# helper function to plot a hist
def plot_a_hist(populations, num_bins, num_steps):
    '''numsteps a tuple (pre_steps, post_steps)
    '''
    pylab.hist(populations, bins=num_bins)
    pylab.xlabel("Value of total viruses' population")
    pylab.ylabel("number of occurrences for "+str(len(populations))+" num of trials")
    pylab.title('Changes to the virus population for '+str(num_steps)+' time steps')

# helper function to calculate the total viruses' population
def total_viruses_population(pre_steps, post_steps=150):
    '''
    gives the total viruses population values for given steps
    pre_steps: <int> the number of steps before treatment
    post_steps: <int> the number of steps after treatment
    
    returns <int> the total viruses' population
    
    '''
    # Initialize the Resistance virus parameters
    maxBirthProb=0.1
    clearProb=0.05
    resistances={'guttagonol': False}
    mutProb=0.005
    # Initialize the Resistant patient parameters
    numViruses=100
    maxPop=1000
    
    # Initialize the total number of steps
    timesteps = [i for i in xrange(pre_steps + post_steps)] # this will be my x-axis
    # Initialize the total viruses' population as an empty list
    accu_total_virus_populations = [0.0 for i in timesteps]
    # Initialize a list of numViruses particles of ResistantVirus
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in xrange(numViruses)]
    # Initialize a Treated Patient with numViruses particles of ResistantVirus
    patient = TreatedPatient(viruses, maxPop)
    
    # For every step
    for timestep in timesteps:
        if timestep == pre_steps: # After pre_steps a give patient a drug
            patient.addPrescription('guttagonol')
        # I calculate the new total population of viruses' particles
        accu_total_virus_populations.append(patient.update())
    return accu_total_virus_populations[-1]

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    
    """
    viruses_population_1 = []
    viruses_population_2 = []
    for trial in xrange(numTrials):
        viruses_population_1.append(total_viruses_population(pre_steps=300, post_steps=150))
        viruses_population_2.append(total_viruses_population(pre_steps=150, post_steps=150))
        

    # PLOTTING
    num_bins = int(max(viruses_population_1)/50)
    pylab.figure(1)
    #
    pylab.subplot(221)
    plot_a_hist(viruses_population_1, num_bins, (300, 150))
    #
    pylab.subplot(222)
    plot_a_hist(viruses_population_2, num_bins, (150, 150))
    #
    pylab.subplot(223)
    plot_a_hist(viruses_population_2, num_bins, (75, 150))
    #
    pylab.subplot(224)
    plot_a_hist(viruses_population_2, num_bins, (0, 150))
    #

#    pylab.legend(loc='best')
    pylab.show()


simulationDelayedTreatment(200)

    
#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
