class Point(object):
    ''' Represents a point in 2-D space'''

    
print Point # <class '__main__.Point'>

blank = Point() # Create object `blank` as an instance of class `Point`
print blank #<__main__.Point object at 0x7fcb2e932350>

#Assign values to instance `blank`
blank.x = 3.0
blank.y = 4.0

#define a function that takes an instance of class Point as an argument
def print_point(p): # p is an alias for object blank
    print '(%g, %g)'%(p.x, p.y)

print_point(blank) # (3, 4)

class Rectangle(object):
    ''' Represents a rectangle
    
    attributes: width, height, corner
    '''

box = Rectangle()
box.width = 100.0 #create and initialize instance var width
box.height = 200.0 #create and initialize instance var height
box.corner = Point() #create instance var corner to be an object of class Point
box.corner.x = 0.0 # create and initialize instance var x of object corner (type Point) to be the instance var of object box (type Rectangle)
box.corner.y = 0.0 # create and initialize instance var y of object corner (type Point) to be the instance var of object box (type Rectangle)

# FUNCTION THAT RETURNS INSTANCES
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0 # 0.0 + 100.0/2.0 
    p.y = rect.corner.y + rect.height/2.0 # 0.0 + 200.0/2.0
    return p

center = find_center(box)
print_point(center) # (50, 100)  

# COPYING OBJECT INSTEAD OF ALIASING
import copy
p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = copy.copy(p1) # now p1 and p2 contain the same data BUT they are different objects
print p1 is p2 #False
print p1 == p2 #False