# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        
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
    
    # TODO
    pre_treatment_steps = 300
    post_treatment_steps = 150
    
    timesteps = [i for i in xrange(pre_treatment_steps + post_treatment_steps)] # this will be my x-axis
    
    accu_total_virus_populations = [0.0 for i in timesteps] # initialize an array with #timesteps=300 zeros
#    accu_resist_virus_populations = [0.0 for i in timesteps] # initialize an array with #timesteps=300 zeros

    for trial in xrange(numTrials):
        viruses = [ResistantVirus(maxBirthProb=0.1, clearProb=0.05, resistances={'guttagonol': False}, mutProb=0.005) for i in xrange(numViruses)] # initialize a list of 100 viruses
        patient = TreatedPatient(numViruses=100, maxPop=1000) #initialize a patient
        for timestep in timesteps:
            if timestep == 150:

                patient.addPrescription('guttagonol')

            accu_total_virus_populations[timestep] += patient.update()

#            accu_resist_virus_populations[timestep] += patient.getResistPop(['guttagonol'])
            
    average_total_viruses_population = [p/float(numTrials) for p in accu_total_virus_populations]
    average_resist_virus_populations = [p/float(numTrials) for p in accu_resist_virus_populations]
    # PLOTTING
    pylab.figure(1)
    pylab.plot(timesteps, average_total_viruses_population, 'ro', label='total virus population')
    pylab.plot(timesteps, average_resist_virus_populations, 'bo', label='resistant virus population')
    pylab.xlabel('Number of time steps')
    pylab.ylabel('Average size of the virus particles population')
    pylab.title('Changes to the virus population for 300 time steps')
    pylab.legend(loc='best')
    pylab.show()


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
    # Initialize the total viruses' population for each timestep to be equal to 0
    accu_total_virus_populations = [0.0 for i in timesteps] # initialize an array with #timesteps=300 zeros
    # Initialize a list of numViruses particles of ResistantVirus
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in xrange(numViruses)]
    # Initialize a Treated Patient with numViruses particles of ResistantVirus
    patient = TreatedPatient(viruses, maxPop)
    
    # For every step
    for timestep in timesteps:
        if timestep == pre_steps: # After pre_steps a give patient a drug
            patient.addPrescription('guttagonol')
        # I calculate the new total population of viruses' particles
        accu_total_virus_populations[timestep] += patient.update()
    return sum(accu_total_virus_populations)
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
