a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

def foo(L):
    val = L[0]
    while (True):
        print 'val = %s and L[val] = %s'%(val, L[val])
        val = L[val]

print foo(c)