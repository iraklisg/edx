def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')

    # calculate the mean values
    MV = sum(len(words) for words in L)/float(len(L)) # list comprehension
    #calculate the sum(x-MV)^2
    res = 0
    for word in L:
        x = len(word)
        res += (x - MV)**2
    #calculate the SD
    SD = (res/float(len(L)))**0.5
    return SD

L1 = ['a', 'z', 'p']
L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L1)
print stdDevOfLengths(L2)
    
            
            
        
