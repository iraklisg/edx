class Point(object):
    def __init__(self, x_cord, y_cord): #x_cord, y_cord are just arguments (values)
        self.orxis = x_cord #self.orxis creates an attribute orxis of an instance of Point (i.e. an object) with the value x_cord
        self.ball = y_cord
        c = 32 # b is a local variable that can be accessed only within the function __init__
    
    def geth(self):
        return self.orxis
    
    def sum(self, b):
        kikirikou = 3
        return self.orxis + self.ball + b

class Point2(Point):
    def __init__(self, orxis, ball, agouri, ntomata):
#        Point.__init__(self, orxis, ball)
        self.orxis = orxis
        self.ball = ball
        self.agouri = agouri
        self.ntomata = ntomata
#        self.salata = self.orxis

    def __str__(self):
        return 'sas enimerwnw oti to x einai %s kai to y einai %s'%(self.orxis, self.ball)
    
class Point3(Point):
    def getY(self):
        return self.ball
    
p1 = Point(3, 4)    


#print p1.orxis
#print p1.sum(3)
##p1.orxis = 4
##p1.ball = 15
#print p1.sum(4)


p2 = Point2(33,44, "a", "b")
print 'tseka',p2.orxis
print p1.orxis
print p2.geth()

p3 = Point3(666, 777)
print p3.ball

print p2