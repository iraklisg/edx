class intSet(object):
    '''is a set of integers
    mpla mpla
    
    '''
    
    def __init__(self):
        """
        Creates an empty list of integers
        
        """
        self.vals = []
        
    def insert(self, e):
        """
        Assume e is an integer
        
        """
        self.vals.append(e)
        
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            print "malakia ekanes, den yparxei to %s"%(e)
            pass # Is a catch an error, just swallow it!!!!
        
    def __str__(self):
        """
        This method is used to alter the defaut representation of
        object `s` (instance of class intSet), when I type
        `print s` in IDLE.
        Otherwise, `print s = <__main__.intSet object at 0x7f6f33a61350>
        
        """
        self.vals.sort()
        return '{'+','.join([str(i) for i in self.vals])+'}'

s = intSet()
s.insert(3)
s.insert(4)
print s
s.remove(5)
print s