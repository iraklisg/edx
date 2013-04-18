class Clock1(object):
    def __init__(self, time):
        self.time = time # this is an attribute of instances (objects) of class Clock
    def print_time(self):
        time = '6:30' # this is a local variable
        print self.time

clock = Clock1('5:30')
clock.print_time() # 5:30 prints out because we printed out the attribute self.time, not the local variable time.

class Clock2(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time): # here a gave parameter (i.e. time) the same name as object attribute (i.e self.time)
        print time

clock = Clock2('5:30')
clock.print_time('10:30')
#What does this problem tell us about giving parameters the same name as object attributes?
#In short, it is needlessly confusing. It is less confusing if you give parameters, local variables, and attributes different, distinct names to avoid the confusion that arises in this problem.

class Clock3(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print self.time 

boston_clock = Clock3('5:30')
paris_clock = boston_clock # boston_clock and paris_clock are two names for the same object. This is called aliasing!!!
paris_clock.time = '10:30'
boston_clock.print_time()