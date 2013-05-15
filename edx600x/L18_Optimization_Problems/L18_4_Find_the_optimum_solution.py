from itertools import *

def allCombos(items):
    # Your code here
    # I have to create all possible combinations(n, k), for k in range len(items+1)
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    for k in range(len(items)+1):
        for combo in list(combinations(items, k)):
            yield list(combo)
         
for i in allCombos(items='ABCD'):
    print i

def powerset(iterable = [1, 2, 3]):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        print 'i =',i
        for j in xrange(N):
            # i is each tie one of all possible 2^N combinations: i.e. 000, 001, 010, 011, etc
            # %2 returns the LSB i.e 010 %2 = 0 , 011 % 2 = 1
            # test bit jth of integer i. If it is 1 then object is taken and added to knapsack
            print 'j = ',j
            print 'i>>j ',i>>j
            print '(i>>j)%2 ',(i>>j)%2
            print 'items[j]', items[j]
            print '------'
            if (i >> j) % 2 == 1: 
                combo.append(items[j])
        yield combo
        print '=========='

# exhaustive search: evaluate each possible combination of items
def chooseBest(pset, maxWeight):
    bestVal = 0.0
    bestSet = None
    for set in pset:
        weight = sum(map(Item.getWeight,set))
        val = sum(map(Item.getValue,set))
        if weight <= maxWeight and val > bestVal:
            bestVal = val
            bestSet = set
    return (bestSet, bestVal)

# look for optimum solution to burglar's problem
def testBest():
    items = buildItems()
    pset = powerSet(items)
    taken, val = chooseBest(pset, 20)
    print 'Total value of items taken =',val
    for item in taken:
        print '  ', item

# build a list of n items of various weights and values
import random
def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in xrange(n)]

# determine average running time of chooseBest with n items
import time
def timeChooseBest(n,ntrials=10):
    # time how long it takes to run chooseBest(items,20)
    def howLong(items):
        pset = powerSet(items)
        start = time.clock()
        chooseBest(pset,20)
        stop = time.clock()
        return stop - start

    # run the specified number of trials
    times = [howLong(buildRandomItems(n))
             for i in xrange(ntrials)]

    print 'Average running time was',sum(times)/ntrials,'seconds.'

########tests
for i in powerSet(['a', 'b', 'c']):
    print (i)

for i in powerset():
    print i