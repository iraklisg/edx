## divisors

def findDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors


divisors = findDivisors(20, 100)
print divisors
total = 0
for d in divisors:
    total += d
print(total)

print range(3,10,2)

x = (1, 2, (3, 'John', 4), 'Hi')
print x

s = 'bananas'
print s[0:-1:2]