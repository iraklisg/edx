class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other_object):
        """
        method that returns True if coordinates refer to same point in the plane
        (i.e., have the same x and y coordinate).
        
        """
        assert type(other_object) == type(self) # make sure `other_object` is of the same type 
        return self.x == other_object.x and self.y == other_object.y # better to use a getter method like self.getX() == other.getX()
        
    def __repr__(self):
        return 'Coordinate(%s, %s)'%(self.getX(), self.getY())


        