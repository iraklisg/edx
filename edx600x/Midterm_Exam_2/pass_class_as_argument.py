class Nikos(object):
    def printaro(self):
        print 'paparia'

def foo(obj):
    return obj()

x = foo(Nikos)
print x.printaro()