

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

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

