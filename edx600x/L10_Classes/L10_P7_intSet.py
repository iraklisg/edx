class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other_list):
        """
        This method would return a new intSet of integers that appear in both s1 and s2.
        Args:
            other_list <intSet>: a list of integers to compare with
        Returns:
            <intset> a list with common integers
        Raises:
            assert that type of other_list is of type self
        
        """
        assert type(other_list) == type(self)
        
#        if len(self.vals) >= len(other_list.vals):
#            big = self.vals
#            small = other_list.vals
#        else:
#            small = self.vals
#            big = other_list.vals
#        
#        common_list = intSet()
#        for e in big:
#            if e in small:
#                common_list.insert(e)
#        return common_list

        common_list = intSet() 
        for e in self.vals:
            if other_list.member(e): #if the current e is a member of other_list
                common_list.insert(e)
        return common_list
        
    
    def __len__(self):
        """This method overwrites the `len` built-in function."""
        return len(self.vals)
            
s1 = intSet()
s2 = intSet()
s1.insert(1)           
s1.insert(2)
s1.insert(3)
s1.insert(4)
s2.insert(3)
s2.insert(4)
s2.insert(5)
s2.insert(6)
s2.insert(7)

print s1
print s2
print s1.intersect(s2) 
print len(s1)
        
            
             
        
