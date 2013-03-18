def logBase2(n):
    """
    assumes that n is a positive int
    returns a float that approximates the log base 2 of n
    """
    import math
    return math.log(n, 2)

print logBase2(1)