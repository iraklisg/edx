L1 = [1,2,3]
L2 = ['a','b','c']

#alliasing
allias_L1_L2 = [L1, L2] #does *not create a new list* BUt it makes a *new empty list that points* in the existing L1 and L2; if L1 changes, then allias changes as well
allias_L1 = L1 # does *not create a new list* BUT an *empty list that points* in to existing L1 list
allias3 = [['k','l','m'],['a','b','c']]

print 'allias_L1_L2 = [L1, L2]                ',allias_L1_L2
print 'allias_L1 = L1                         ',allias_L1
print 'allias3                                ',allias3

#flattening mesw concatenate (+)
flat = L1 + L2 #creates *new independent list* *without pointers* to previous L1, L2
print 'flat  = L1 + L2                        ', flat

#cloning
clon = L1[:] #creates a total *new list* *without pointers*
print 'clon =L1[:]                            ',clon

print '====================[ MUTATION ]====================='

z = allias3[0]
print 'z = allias3[0]                          ',z

L1.append(666)
print 'L1.append(666)'

allias_L1.append(777)
print 'allias_L1.append(777)'

allias_L1_L2[1][-1] = 'zzzz'
print 'allias_L1_L2[1][-1] = zzzz'

allias3[0].append(888)
print 'allias3[0].append(888)'




print '======================================================'
print 'L1 after mutation (appending)          ',L1
print '======================================================'
print 'allias_L1_L2 after appending to L1     ',allias_L1_L2
print 'allias_L1 after appending to allias_L1 ',allias_L1 
print 'allias3 after appending to allia3      ',allias3 
print 'flat after appending to L1             ',flat
print 'clon after appending 6 to L1           ',clon
print 'z after appending on allias3           ',z


