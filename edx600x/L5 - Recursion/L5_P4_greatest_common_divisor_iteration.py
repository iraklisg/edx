def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = min(a, b)
    print 'initial gcd =',gcd
    while gcd > 0:
        print 'a%gcd =',a%gcd
        print 'b%gcd =',b%gcd
        if a%gcd !=0 or b%gcd != 0:
            gcd -= 1
        else:
            break
    return gcd

x = 17
y = 12

z=gcdIter(x, y)
print 'z =',z
