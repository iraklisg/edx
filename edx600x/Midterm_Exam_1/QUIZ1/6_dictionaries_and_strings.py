def f(s, d):
    for k in d.keys():
        d[k] = 0
    for c in s:
        if c in d:
            d[c] +=1
        else:
            d[c] = 0
    return d

def addUp(d):
    result = 0
    for k in d:
        result += d[k]
    return result

d1 = {}
d2 = d1
d1 = f('abbc', d1)
print 'd1 =',d1
print addUp(d1)
d2 = f('bbcaa', d2)
print 'd2 =',d2
print addUp(d2)
print 'd1 due to alliasing =',d1
print f('', {})
print result # name error because "result" is not defined!!!