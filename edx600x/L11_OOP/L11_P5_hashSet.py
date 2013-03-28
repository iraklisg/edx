class hashSet(object):
    def __init__(self, numBuckets): 
        '''
        numBuckets: int. The number of buckets this hash set will have. 
        Raises ValueError if this value is not an integer, or if it is not greater than zero.
    
        Sets up an empty hash set with numBuckets number of buckets.
        
        '''
        if type(numBuckets) != int or numBuckets <= 0:
            raise ValueError()
        self.numBuckets = numBuckets 
        self.hashSet = []
        for bucket in range(self.numBuckets):
            self.hashSet.append([])
    
    def hashValue(self, e):
        '''
        e: an integer
    
        returns: a hash value for e, which is simply e modulo the number of 
         buckets in this hash set. Raises ValueError if e is not an integer.
        
        '''
        if type(e) != int:
            raise ValueError()
        
        return e % self.numBuckets
    
    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        
        '''
        if type(e) != int:
            raise ValueError()
        
        for bucket in self.hashSet:
            if e in bucket:
                return True
        return False

    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        
        '''
        if type(e) != int:
            raise ValueError()
        
        num_of_bucket = self.hashValue(e) # it should be either 0 or 1 or 2 ... or self.numBuckets - 1
        self.hashSet[num_of_bucket].append(e)

    def remove(self, e):
        '''
        e: is an integer 
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        
        '''
        if type(self.numBuckets) != int:
            raise ValueError()
        
        flag = 0
        for bucket in self.hashSet:
            if e in bucket: flag += 1 # it should be at most in one bucket
        if flag == 0: # means there wasn't in any bucket 
            raise ValueError()
        
        num_of_bucket = self.hashValue(e) # e should be either on bucket 0 or 1 or 2 ... or self.numBuckets - 1
        self.hashSet[num_of_bucket].remove(e)
        
    def getNumBuckets(self):
        return self.numBuckets
    
    def __str__(self):
        return str(self.hashSet)
        
obj = hashSet(3)
print obj.hashSet
print obj.hashValue(7)
obj.insert(7)
obj.insert(8)
obj.insert(9)
obj.insert(11)
print obj.hashSet
obj.remove(9)
print obj
