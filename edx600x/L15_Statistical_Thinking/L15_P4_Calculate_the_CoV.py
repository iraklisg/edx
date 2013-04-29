l = [10, 4, 12, 15, 20, 5]

def stdDev(X):
    """
    Calculate the SD of a given data set
    X: a list with data
    returns: the SD as (1/X sum(X-Mean)**2)**0.5
    
    """
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def CoV(X):
    """
    Calculate the CoV for a given data set X.
    X: a list
    
    returns: The CoV = SD/Mean = (1/X sum(X-Mean)**2)**0.5 / Mean
    
    """
    SD = stdDev(X)
    mean = sum(X)/float(len(X))
    return SD/mean

print CoV(l)