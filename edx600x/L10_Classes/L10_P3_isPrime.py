def isPrime(n):
    if type(n) != int:
        raise TypeError()
    if n <= 0:
        raise ValueError()
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i += 1
    return True

print isPrime(-4)    