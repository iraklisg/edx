def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def greedy(items, maxWeight, metric):
    knapsack = []
    totalW = 0
    # process items in order of metric, biggest first
    for item in sorted(items, key=metric, reverse=True):
        w = item.getWeight()
        # if item will fit in knapsack, take it!
        if w + totalW <= maxWeight:
            knapsack.append(item)
            totalW += w
    return knapsack
            
# metric: use item's value
def value(item):
    return item.getValue()

# metric: use item's "lightness" = inverse of weight
def weightInverse(item):
    return 1.0/item.getWeight()

# metric: use item's value/weight
def density(item):
    return item.getValue()/item.getWeight()

# try greedy algorithm with given metric, print result
def testGreedy(items, maxWeight, metric):
    taken = greedy(items, maxWeight, metric)
    val = sum(map(Item.getValue,taken))
    print 'Total value of items taken = ', val
    for item in taken:
        print '  ', item

# try greedy algorithm with all three metrics
def testGreedys(maxWeight = 20):
    items = buildItems()
    print 'Items to choose from:'
    for item in items:
        print '  ', item
    print 'Use greedy by value to fill a knapsack of size', maxWeight
    testGreedy(items, maxWeight, value)
    print 'Use greedy by weight to fill a knapsack of size', maxWeight
    testGreedy(items, maxWeight, weightInverse)
    print 'Use greedy by density to fill a knapsack of size', maxWeight
    testGreedy(items, maxWeight, density)

