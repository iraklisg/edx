# allow many levels of recursion while we're experimenting
import sys
sys.setrecursionlimit(5000)

############################################################
############################################################
###
### fibonacci & memoize
###
############################################################
############################################################

# the classic fibonacci function
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# works for functions with hashable (immuatble) arguments
# Example usage: fib = memoize(fib)
def memoize(f):
    # define "wrapper" function that checks cache for
    # previously computed answer, only calling f if this
    # is a new problem.
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]

    # initialize wrapper function's cache.  store cache as
    # attribute of function so we can look at its value.
    memf.cache = {}
    return memf

############################################################
############################################################
###
### 0/1 knapsack
###
############################################################
############################################################

# from earlier lecture...
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __repr__(self):
        return 'Item(' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + ')'

# choose most valuable selection of items that will fit
# returns (total_value,item_sequence)
def chooseBest(items,maxWeight):
    if len(items) == 0 or maxWeight <= 0:
        return (0,())
    first = items[0]
    w = first.getWeight()
    rest = items[1:]

    # alternative 1: don't include first item in knapsack
    v1,t1 = chooseBest(rest,maxWeight)

    # alternative 2: include first item in knapsack
    # remember to leave room for first item in knapsack
    v2,t2 = chooseBest(rest,maxWeight - w)
    v2 += first.getValue()  # now include first item
    t2 += (first,)

    # choose most valuable alternative (choice 2 is
    # possible only if first item fits in knapsack)
    return (v2,t2) if w <= maxWeight and v2 >= v1 else (v1,t1)

fewItems = tuple(Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                            ('painting', 90, 9),
                                            ('radio', 20, 4),
                                            ('vase', 50, 2),
                                            ('book', 10, 1),
                                            ('computer', 200, 20)))

# build a tuple of n items of various weights and values
import random
def buildRandomItems(n):
    return tuple(Item(str(i),
                       10*random.randint(1,10),
                       random.randint(1,5))
                  for i in xrange(n))

# chooseBest(manyItems,20) completes only if chooseBest is memoized
manyItems = buildRandomItems(50)

def testChooseBest(items,maxWeight):
    value, result = chooseBest(items,maxWeight)
    print '*** total value of items in knapsack =',value
    for item in result: print '    ',item

############################################################
############################################################
###
### choosing line breaks
###
############################################################
############################################################

# determine optimal line breaks to minimize sum of (maxWidth - lineWidth)**3
# returns (paragraph_string,cost)
def lineBreaks(wlist,startCol,maxWidth):
    if len(wlist) == 0:
        # reached end of word list, yah!
        return ("", 0)
    word = wlist[0]
    rest = wlist[1:]
    endCol = len(word) + startCol

    # word doesn't fit on line, signal infinite cost
    if endCol > maxWidth:
        return ("",1e9)   # an "infinite" cost

    # alternative 1: no line break after word.  Rest of the words
    # placed starting after the current word; remember to
    # leave room for the separating space!
    r1,c1 = lineBreaks(rest,endCol+1,maxWidth)
    r1 = word + " " + r1

    # alternative 2: line break after word. Rest of the words
    # placed starting on a newline.
    r2,c2 = lineBreaks(rest,0,maxWidth)
    r2 = word + "\n" + r2
    c2 += (maxWidth - endCol)**3  # compute end of line penalty

    # choose least costly alternative
    return (r1,c1) if c1 <= c2 else (r2,c2)

# determine breaks by adding words until line is full
# returns (paragraph_string, cost)
def greedyBreaks(wlist,maxWidth):
    cost = 0
    result = ""
    col = 0
    for word in wlist:
        endCol = col + len(word)
        if col != 0: endCol += 1
        if endCol > maxWidth:
            cost += (maxWidth - col)**3
            result += '\n'
            col = 0
        if col != 0:
            result += ' '
            col += 1
        result += word
        col += len(word)
    return(result,cost)

# try width = 13
wlist1 = tuple("This may be a difficult example".split(' '))

# try width = 40.  Only completes when lineBreaks is memoized
wlist2 = tuple("Four score and seven years ago our fathers brought forth on this "
               "continent a new nation, conceived in liberty, and dedicated to the "
               "proposition that all men are created equal.  Now we are engaged in "
               "a great civil war, testing whether that nation, or any nation, so "
               "conceived and so dedicated, can long endure. We are met on a great "
               "battlefield of that war. We have come to dedicate a portion of that "
               "field, as a final resting place for those who here gave their lives "
               "that that nation might live. It is altogether fitting and proper that "
               "we should do this.".split(' '))

def testBreaks(wlist,width):
    result,cost = lineBreaks(wlist,0,width)
    print '*** lineBreaks cost =',cost
    print result

    result,cost = greedyBreaks(wlist,width)
    print '\n*** greedyBreaks cost =',cost
    print result

############################################################
############################################################
###
### sequence alignment
###
############################################################
############################################################

mcost = 1    # penalty for a symbol mismatch
gcost = 1    # penalty for introducing a gap

# find min cost alignment of two strings.  There may be gaps
# and/or changed symbols in each string.
# returns (aligned_s1,aligned_s2,cost)
def align(s1,s2):
    if len(s1) == 0:
        # s1 has run out, so assume it's padded with gaps
        l = len(s2)
        return ('-'*l,s2,gcost*l)

    if len(s2) == 0:
        # s2 has run out, so assume it's padded with gaps
        l = len(s1)
        return (s1,'-'*l,gcost*l)

    # alternative 1: align s1[0] and s2[0]
    # pay mismatch penalty, if any, for alignment, align rest
    c1_1,c1_2,c1_cost = align(s1[1:],s2[1:])
    c1_1 = s1[0] + c1_1   # add s1[0] to front of aligned s1
    c1_2 = s2[0] + c1_2   # add s2[0] to front of aligned s2
    if s1[0] != s2[0]:
        c1_cost += mcost  # mismatch penalty
        # beautification: use lower case to signal mismatch
        c1_1 = c1_1[0].lower() + c1_1[1:]
        c1_2 = c1_2[0].lower() + c1_2[1:]

    # alternative 2: s1[0] aligns with a gap at front of s2
    # pay gap penalty, align rest of s1 with all of s2
    c2_1,c2_2,c2_cost = align(s1[1:],s2)
    c2_1 = s1[0] + c2_1   # add s1[0] to front of aligned s1
    c2_2 = '-'   + c2_2   # gap at front of aligned s2
    c2_cost += gcost      # gap penalty

    # alternative 3: s2[0] aligns with a gap at front of s1
    # pay gap penalty, align rest of s2 with all of s1
    c3_1,c3_2,c3_cost = align(s1,s2[1:])
    c3_1 = '-'   + c3_1   # gap at front of aligned s1
    c3_2 = s2[0] + c3_2   # add s2[0] to front of aligned s2
    c3_cost += gcost      # gap penalty

    # return alternative with min cost
    if c1_cost <= c2_cost and c1_cost <= c3_cost:
        return (c1_1,c1_2,c1_cost)
    elif c2_cost <= c1_cost and c2_cost <= c3_cost:
        return (c2_1,c2_2,c2_cost)
    else:
        return (c3_1,c3_2,c3_cost)

# expect CAT
#        -AT
s1a = 'CAT'
s1b = 'AT'

# only completes when align is memoized
# expect -CTGACCTACcT
#        CCTGAC-TACaT
s2a = 'CTGACCTACCT'
s2b = 'CCTGACTACAT'

def testAlign(s1,s2):
    a1,a2,cost = align(s1,s2)
    print 'aligned s1:',a1
    print 'aligned s2:',a2
    print '*** cost =',cost