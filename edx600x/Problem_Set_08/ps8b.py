# Problem Set 8: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab
#from ps8b_precompiled_27 import *  

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb


    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        
        """
        # I want the function doesClear to return True with probability self.getClearProb i.e 1 out of self.getClearProb times
        # random() return a numbers 'k' between 0 to 1 with equal probability (uniform distributed)
        # Therefore, if I run random 1,000,000 times, it will give me numbers <0.4 400,000 times
        # i.e the returned numbers will occur 40/100 times, that is with probability 0.4
        k = random.random() # generate a random number k between 0 - 1 with equal probability
        if k <= self.getClearProb(): return True # if that number k is less or equal to self.getClearProb() return True
        else: return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.getMaxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        
        """
        p_virus_reproduced = self.getMaxBirthProb() * (1 - popDensity) # the probability of a virus to be reproduced.
        if random.random() <= p_virus_reproduced:
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException
            



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        
        """
        viruses_copy = self.viruses[:] #create a copy of viruses list
        for virus_particle in viruses_copy:
            if virus_particle.doesClear(): #if True, i.e a virus particle has been cleared (prob. 100*clearProb %)
                self.viruses.remove(virus_particle) # update viruses list by removing virus particles that have been not cleared
        
        # calculate the uncleared viruses  population density given current viruses population and max viruses population 
        current_viruses_population = self.getTotalPop()
        max_viruses_population = self.getMaxPop()
        viruses_population_density = current_viruses_population / float(max_viruses_population) # is the popDensity argument of the SimpleVirus.reproduce() method
        
        
        viruses_copy = self.viruses[:] #create a new copy of viruses list
        for virus_particle in viruses_copy: # for the remaining particles of virus
            # try to breed an offspring; reproduction is Based on the value of population density 
            try: # see if a particle will breed offsprings (prob. of breeding an offspring is self.getMaxBirthProb * (1 - popDensity)
                self.viruses.append(virus_particle.reproduce(viruses_population_density)) # if no NoChildException exception is raised from reproduce() do the append
            except NoChildException:
                pass
        
        return self.getTotalPop()
                


#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    
    """
    viruses = [SimpleVirus(maxBirthProb, clearProb) for i in xrange(numViruses)] # initialize a list of 100 viruses
    arostiaris = Patient(viruses, maxPop) #initialize a patient
    
    number_of_steps = 300
    timesteps = [t for t in range(number_of_steps)] # this will be my x-axis
    accu_virus_populations = [0 for i in timesteps] # initialize an array with #timesteps=300 zeros
    
    for trial in xrange(numTrials):
        for timestep in timesteps:
            current_population = arostiaris.update()
            accu_virus_populations[timestep] += current_population #appends the population for every time step
            
    average_viruses_population = [p/float(numTrials) for p in accu_virus_populations]
    # PLOTTING
    pylab.figure(1)
    pylab.plot(timesteps, average_viruses_population, 'ro', label='SimpleVirus particles population')
    pylab.xlabel('Number of time steps')
    pylab.ylabel('Average size of the SimpleVirus particles population')
    pylab.title('Changes to the virus population for 300 time steps')
    pylab.legend()
    pylab.show()
    
def simulationWithoutDrugNick(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    #Instantiate the viruses first, the patient second
    viruses= [ SimpleVirus(maxBirthProb, clearProb) for i in range(numViruses) ]
    patient = Patient(viruses, maxPop)
    #Execute the patient.update method 300 times for 100 trials
    steps = 300
    countList = [0 for i in range(300)]
    for trial in range(numTrials):
        for timeStep in range(steps):
            countList[timeStep] += patient.update()
    avgList = [ countList[i]/float(numTrials) for i in range(steps) ]
    #Plot a diagram with xAxis=timeSteps, yAxis=average virus population
    xAxis = [ x for x in range(steps) ]
    pylab.figure(2)
    pylab.plot(xAxis, avgList, 'ro', label='Simple Virus')
    pylab.xlabel('Number of elapsed time steps')
    pylab.ylabel('Average size of the virus population')
    pylab.title('Virus growth in a patient without the aid of any drag')
    pylab.legend()
    pylab.show()


# PROBLEM 4

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        
        """
        if self.resistances.get(drug,0) == True:
            return True
        else:
            return False


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.getMaxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb, clearProb, and mutProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        
        """
        prob_reproduction = self.getMaxBirthProb() * (1 - popDensity)
#        print 'probability of reproduction is', prob_reproduction
        # check if virus is resistance to ALL active drugs
        for drug in activeDrugs:
            if self.isResistantTo(drug) == False:
#                print "no children"
                raise NoChildException
                break
        else: #for/else clause will NOT be executed when loop hits the break statement
        # if the virus IS resistance to ALL drugs
        # randomly see whether the virus will reproduced given the prob_reproduction
            if random.random() <= prob_reproduction: # if yes
                #initialize the resistances of offspring
                child_resistances = self.getResistances().copy()
                # define the possible mutation in resistance according to the self.mutProb
                for drug in self.getResistances():
#                    gg = random.random()
                    if random.random() <= self.getMutProb():
#                        print 'checking %s with prob %f'%(drug, gg)
                        child_resistances[drug] = not self.getResistances().get(drug, 0)
                # return the offspring with the possible mutated self.resistances
                return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), child_resistances, self.getMutProb())
            else:
#                print 'ggg'
                raise NoChildException
            
        # TODO

            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        
        """
        Patient.__init__(self, viruses, maxPop)
        #initialize a list with all drugs administered to the patient
        self.prescription_list = [] 


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        
        """
        if newDrug not in self.prescription_list:
            self.prescription_list.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        
        """
        return self.prescription_list
    

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        
        """
        count = 0 # initialize the counter of the pop. of viruses with resistances to ALL drugs in dtugResist list
        #for every virus in the self.viruses list
        for virus in self.viruses:
            #for every drug in drugResist (search exhaustively in the drugResist list)
            for drug in drugResist:
                # if that drug is in the resistances dict. of that particular virus
                # and that virus IS NOT resistant to that drug (False)
                if virus.resistances.get(drug, 0) == False: # if that drug not exist in virus' resistances, returns 0 == False (hit break); else returns True/False
                    break
            else: # if break is not executed, i.e. virus IS resistant to ALL drugs in drugResist list
                count += 1
        return count


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        
        """
        # Determine which viruses have been cleared by drugs prescription
        # ATTENTION: The drugs we consider DO NOT directly kill (i.e. remove()) virus particles lacking resistance to the drug
        # but prevent those virus particles from reproducing
        viruses_copy = self.viruses[:] #create a copy of viruses list
        for virus_particle in viruses_copy:
            for drug in self.getPrescriptions():
                if virus_particle.resistances.get(drug) == False: #If this virus IS NOT resistant to that prescription drug
                    virus_particle.maxBirthProb = 0 # Do not kill it, just give it no chance to reproduce
        
        # Determine which viruses particles remain after been cleared by immune system
        viruses_copy = self.viruses[:] #create a copy of viruses list
        for virus_particle in viruses_copy:
            if virus_particle.doesClear(): #if True, i.e a virus particle has been cleared by immune system (prob. 100*clearProb %)
                self.viruses.remove(virus_particle) # update viruses list by removing virus particles that have been not cleared
                
        
        # calculate the uncleared viruses  population density given current viruses population and max viruses population 
        current_viruses_population = self.getTotalPop()
        max_viruses_population = self.getMaxPop()
        viruses_population_density = current_viruses_population / float(max_viruses_population) # is the popDensity argument of the SimpleVirus.reproduce() method
        
        
        viruses_copy = self.viruses[:] #create a new copy of viruses list
        for virus_particle in viruses_copy: # for the remaining particles of virus
            # try to breed an offspring; reproduction is Based on the value of population density 
            try: # see if a particle will breed offsprings (prob. of breeding an offspring is self.getMaxBirthProb * (1 - popDensity)
                self.viruses.append(virus_particle.reproduce(viruses_population_density, self.getPrescriptions())) # if no NoChildException exception is raised from reproduce() do the append
            except NoChildException:
                pass
        
        return self.getTotalPop()

        # TODO



#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """


    steps = 300
    timesteps = [i for i in xrange(steps)] # this will be my x-axis
    
    accu_total_virus_populations = [0.0 for i in timesteps] # initialize an array with #timesteps=300 zeros
    accu_resist_virus_populations = [0.0 for i in timesteps] # initialize an array with #timesteps=300 zeros
#    arxidia = []
    for trial in xrange(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in xrange(numViruses)] # initialize a list of 100 viruses
        patient = TreatedPatient(viruses, maxPop) #initialize a patient
        for timestep in timesteps:
            if timestep == 150:
#                print '149!!!!!!!!!!!!!11'
                patient.addPrescription('guttagonol')
#                print patient.getPrescriptions() 
            accu_total_virus_populations[timestep] += patient.update()
#            print patient.getPrescriptions()
            accu_resist_virus_populations[timestep] += patient.getResistPop(['guttagonol'])
#            if patient.getPrescriptions() == ['guttagonol'] :
#                arxidia.append(1)
#            else:
#                arxidia.append(0)
                
            
#            accu_total_virus_populations[timestep] += current_total_population #appends the population for every time step
#            accu_resist_virus_populations[timestep] += current_resist_population #appends the population for every time step

            
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
#    print arxidia
#    print sum(arxidia)
#    print len(arxidia)

simulationWithDrug(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05, resistances={'guttagonol': False},
                       mutProb=0.005, numTrials=100)
    
#################### TESTS
#virus = SimpleVirus(1.0, 0.0)
#patient = Patient([virus], 100)
#print patient.update()
#
#random.seed(0)
#simulationWithoutDrug(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, clearProb = 0.05, numTrials = 100)
##################### test scenario 2
#virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
#popDensity = 0.0
#offsprings = []
#for i in xrange(10):
#    offsprings.append(virus.reproduce(0, []))
#    print 'offspring %d resistances %s'%(i,offsprings[i].getResistances())
#print 'and the father', virus.getResistances()
################# test scenario getResistPop
#virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
#virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
#virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
#patient = TreatedPatient([virus1, virus2, virus3], 100)   
#
#print patient.getResistPop(['drug2'])
################# test scenario virus populations in treated patient
#virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0) #always reproduce, never mutates and never cleared by immune system
#virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
#patient = TreatedPatient([virus1, virus2], 1000000)
#patient.addPrescription("drug1")
#
#for i in xrange(5):
#    patient.update()
#
#print patient.getResistPop(patient.getPrescriptions())
#print patient.getTotalPop()

#random.seed(0)

#random.seed(0)
# simulationWithoutDrugNick(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, clearProb = 0.05, numTrials = 100)