# Example 1 - itsProblem is a LOCAL VARIABLE
class Example1(object):
    def the_example(self):
        itsProblem = "problem"

theExample = Example1()
#print(theExample.itsProblem) # AttributeError: 'Example1' object has no attribute 'itsProblem'

# Example 2 - itsProblem is an INSTANCE (aka OBJECT) VARIABLE
class Example2(object):
    def __init__(self):
        self.itsProblem = "problem"

theExample = Example2()
print(theExample.itsProblem) # problem

# Example 3 - itsProblem is a CLASS (aka STATIC) VARIABLE
class Example3(object):
    itsProblem = "problem"


theExample = Example3()
print(theExample.itsProblem)
print (Example3.itsProblem)  # But be careful with this one, as theExample.itsProblem is automatically set
                            # to be equal to Example.itsProblem, but is not the same variable at all and
                            # can be changed independently.

# You'll notice we first set a class variable, then we access an object variable (theExample.itsProblem).
# We never set this object variable but it works, how is that possible?
# Well, Python tries to get first the object variable, but if he can't find it, will give you the class variable.
# Warning: the class variable is shared among instances, and the object variable is not.

class Example4(object):
    pass

Example4.itsProblem = "problem" # set a class variable

e = Example4()
e.itsSecondProblem = "problem" # create an object variable

print Example4.itsProblem == e.itsSecondProblem 
print Example4.itsProblem is e.itsSecondProblem 
e.itsSecondProblem = "answer"
print Example4.itsProblem == e.itsSecondProblem 
print Example4.itsProblem is e.itsSecondProblem 