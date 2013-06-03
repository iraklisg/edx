a = [0,1,2,3,4,5,6,7,8]
b = [5,10,10,10,15]
c = [0,1,2,4,6,8]
d = [6,7,11,12,13,15]
e = [9,0,0,3,3,3,6,6]

list = [a, b, c, d, e]

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (mean, (tot/len(X))**0.5)

# mean, sd = stdDev(a)
# print "mean = {} and sd = {}".format(mean, sd)

for sublist in list:
    mean, sd = stdDev(sublist)
    print "list = {}, mean = {} and sd = {}".format(sublist, mean, sd)
    
###########

def m2(l):
    return sum(l)/len(l)

def v2(l):
    mu = m2(l)
    temp = 0
    for e in l:
        temp += (e-mu)**2
    return temp / len(l)

for l in list:
    m = m2(l)
    v = v2(l)
    print "m2  = {} , v2 = {}".format(m, v)

x="x={0}{1}{0}; print x.format(chr(34),x)"; print x.format(chr(34),x)

x = [2,1]
y = [2,1]
print x == y

print y.sort()
print x
print sorted(y)