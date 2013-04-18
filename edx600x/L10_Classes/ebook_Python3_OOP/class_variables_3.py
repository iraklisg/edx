class Example(object):
    itsProblem = [1,2,3]
    def __init__(self):
        self.itsProblem = []
        self.itsProblem.append('kikirikou')
    def add (self):
        self.itsProblem = []
            


a = Example()

print a.itsProblem
print Example.itsProblem
a.add()
print a.itsProblem
print Example.itsProblem
a.itsProblem.append('marmara')
print a.itsProblem
print Example.itsProblem

#  Note that an object variable with the same name as a class variable will hide the class variable! 