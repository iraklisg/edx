from itertools import *



def dec2ternary(num):
    result = ''
    while num > 0:
        result = str(num%3)+result
        num = num/3
    return list(result)

print dec2ternary(7)

def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            if (i / 3**j) % 3 == 1: 
                bag1.append(items[j])
            elif (i / 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        
for i in yieldAllCombos(items='ABC'):
    print i

