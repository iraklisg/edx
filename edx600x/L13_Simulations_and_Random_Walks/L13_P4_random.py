import random, pylab

class SomeDict(object): # Abstract class to create a dict object
    def __init__(self, name):
        self.d = {}
        self.name = name
        
    def __str__(self):
        return self.name
        
        
class PlotDict(object): # Mix-in class to print a dict
    def plot_dict(self):
        rand_num = self.d.keys() # get a list of randomly produced numbers x belong to [0, 9)
        num_occur = self.d.values() # get a list with the number of times the x number appears after generating them 10000 times
    #    print 'rand_num',rand_num
    #    print "num_occur",num_occur
        
        sorted_rand_num = sorted(rand_num) # create a sorted list of keys
        sorted_num_occur = [self.d[key] for key in sorted_rand_num] # create a list of values according to the sorted keys 
        
    #    print "sorted_rand_num",sorted_rand_num
    #    print "sorted_num_occur",sorted_num_occur
        pylab.figure(PlotDict.__name__)
        pylab.plot(sorted_rand_num,sorted_num_occur) # plot the sorted <key, value> pairs
        pylab.show()


class RandrangeDict(PlotDict, SomeDict): # subclass of SomeDict that creates a dic with keys =  nums between 0 1nd 10 and values = the number of ocurrences of each number 
    def __init__(self, name):
        SomeDict.__init__(self, name)
        for i in range(10000):
            x = random.randrange(10) 
            self.d[x] = self.d.get(x, 0) + 1


class RandomDict(PlotDict, SomeDict): # subclass of SomeDict that creates a dic with keys =  nums between 0 1nd 10 and values = the number of ocurrences of each number 
    def __init__(self, name):
        SomeDict.__init__(self, name)
        for i in range(10000):
            x = int(random.random()*10)
            self.d[x] = self.d.get(x, 0) + 1


class RandintDict(PlotDict, SomeDict): # subclass of SomeDict that creates a dic with keys =  nums between 0 1nd 10 and values = the number of ocurrences of each number 
    def __init__(self, name):
        SomeDict.__init__(self, name)
        for i in range(10000):
            x = random.randint(0, 10)
            self.d[x] = self.d.get(x, 0) + 1
    
#########################################################

d1 = RandrangeDict("randrange")
d2 = RandomDict("random")
d3 = RandintDict("randint")
d1.plot_dict()
d2.plot_dict()
d3.plot_dict()
