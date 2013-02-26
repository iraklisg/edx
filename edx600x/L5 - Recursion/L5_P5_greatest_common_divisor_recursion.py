def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # base case b=0
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

print gcdRecur(17, 12)