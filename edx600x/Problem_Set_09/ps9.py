# 6.00 Problem Set 9

import numpy
import random
import pylab
#from ps8b import *
from ps8b_precompiled_27 import *

#random.seed(0)
#
# PROBLEM 1
# helper function to plot a hist
def plot_a_hist(data, num_bins, axe, title):
    '''
        numsteps a tuple (pre_steps, post_steps)
        axes: a tuple of tuples
    '''       
    axe.hist(data, bins=num_bins, histtype='bar', cumulative=True, normed=1)
    axe.set_xlabel("Value of total viruses' population")
    axe.set_ylabel("number of occurrences for "+str(len(data))+" num of trials")
    axe.set_title(title)


# helper function to calculate the total viruses' population
def total_viruses_population_1(pre_steps, post_steps):
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
    numViruses=200
    maxPop=1000
    
    # Initialize the total number of steps
    timesteps = [i for i in xrange(pre_steps + post_steps)] # this will be my x-axis
    # Initialize the total viruses' population as an empty list
    accu_total_virus_populations = []
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
    viruses_population_1 = [] # delay 300
    viruses_population_2 = [] # delay 150
    viruses_population_3 = [] # delay 75
    viruses_population_4 = [] # delay 0
    
    for trial in xrange(numTrials):
        viruses_population_1.append(total_viruses_population_1(300, 150))
        viruses_population_2.append(total_viruses_population_1(150, 150))
        viruses_population_3.append(total_viruses_population_1(75, 150))
        viruses_population_4.append(total_viruses_population_1(0, 150))
        
    # PLOTTING
    # Define the num of bins
    num_bins = int(max(viruses_population_1)/10) # to evenly divide x-axis space in 10 bins
    # Initialize the subplots to be used
    f, ((ax1, ax2), (ax3, ax4)) = pylab.subplots(2, 2, sharex='col', sharey='row') #sharex='col', sharey='row'
    plot_a_hist(viruses_population_1, num_bins, ax1, 'Changes to the virus population for delay on 1st drug administration ='+str(300))
    plot_a_hist(viruses_population_2, num_bins, ax2, 'Changes to the virus population for delay on 1st drug administration ='+str(150))
    plot_a_hist(viruses_population_3, num_bins, ax3, 'Changes to the virus population for delay on 1st drug administration ='+str(75))
    plot_a_hist(viruses_population_4, num_bins, ax4, 'Changes to the virus population for delay on 1st drug administration ='+str(0))

#
# PROBLEM 2
#
# helper function to calculate the total viruses' population
def total_viruses_population_2(steps_pre_drug1, steps_pre_drug2, post_steps):
    '''
    gives the total viruses population values for given steps
    pre_steps: <int> the number of steps before treatment
    post_steps: <int> the number of steps after treatment
    
    returns <int> the total viruses' population
    
    '''
    # Initialize the Resistance virus parameters
    maxBirthProb=0.1
    clearProb=0.05
    resistances={'guttagonol': False, 'grimpex': False}
    mutProb=0.005
    # Initialize the Resistant patient parameters
    numViruses=100
    maxPop=1000
    
    # Initialize the total number of steps
    timesteps = [i for i in xrange(steps_pre_drug1 + steps_pre_drug2 + post_steps)] # this will be my x-axis
    # Initialize the total viruses' population as an empty list
    accu_total_virus_populations = []
    # Initialize a list of numViruses particles of ResistantVirus
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in xrange(numViruses)]
    # Initialize a Treated Patient with numViruses particles of ResistantVirus
    patient = TreatedPatient(viruses, maxPop)
    
    # For every step
    for timestep in timesteps:
        if timestep == steps_pre_drug1: # After pre_steps a give patient 1st drug
            patient.addPrescription('guttagonol')
        if timestep == steps_pre_drug1+steps_pre_drug2: # After pre_steps a give patient 1st drug
            patient.addPrescription('grimpex')
        # I calculate the updated total population of viruses' particles
        accu_total_virus_populations.append(patient.update())
    return accu_total_virus_populations[-1]


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
    viruses_population_1 = [] # delay 300
    viruses_population_2 = [] # delay 150
    viruses_population_3 = [] # delay 75
    viruses_population_4 = [] # delay 0
    
    for trial in xrange(numTrials):
        viruses_population_1.append(total_viruses_population_2(150, 300, 150))
        viruses_population_2.append(total_viruses_population_2(150, 150, 150))
        viruses_population_3.append(total_viruses_population_2(150, 75, 150))
        viruses_population_4.append(total_viruses_population_2(150, 0, 150))
        
    # PLOTTING
    # Define the num of bins
    num_bins = int(max(viruses_population_1)/10) # to evenly divide x-axis space in 10 bins
    # Initialize the subplots to be used
    f, ((ax1, ax2), (ax3, ax4)) = pylab.subplots(2, 2, sharex='col', sharey='row') #sharex='col', sharey='row'
    plot_a_hist(viruses_population_1, num_bins, ax1, 'Changes to the virus population for delay on 2nd drug administration ='+str(300))
    plot_a_hist(viruses_population_2, num_bins, ax2, 'Changes to the virus population for delay on 2nd drug administration ='+str(150))
    plot_a_hist(viruses_population_3, num_bins, ax3, 'Changes to the virus population for delay on 2nd drug administration ='+str(75))
    plot_a_hist(viruses_population_4, num_bins, ax4, 'Changes to the virus population for delay on 2nd drug administration ='+str(0))

############
#MAIN
simulationDelayedTreatment(100)
simulationTwoDrugsDelayedTreatment(100)
pylab.show()
