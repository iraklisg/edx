def genPrimes():
    prime_numbers = [] # singleton with the first prime number as initialization
    x = 2 # the next prime number
    flag = 1 # not 0 in order to print the first yield with x = 2
    while True:
        if flag != 0: 
            # x is a prime number
            prime_numbers.append(x)
            yield x
        x += 1 # now check the next natural number if it is a prime number
        # A candidate number x is prime if (x % p) != 0 for all earlier primes p
        x_mod_p = [x % p for p in prime_numbers] # (x % p) for all earlier primes p
        flag = reduce(lambda x, y: x*y, x_mod_p) # if (x % p) != 0 ==> flag != 0 
        
''' Alternative solution using for/else clause '''
#def genPrimes():
#    primes = []   # primes generated so far
#    last = 1      # last number tried
#    while True:
#        last += 1
#        for p in primes:
#            if last % p == 0:
#                break
#        else: # else is NOT executed if for loop is terminated by break; is executed when loop is terminated through exhaustion of list in for
#            primes.append(last)
#            yield last

for number in genPrimes():
    print number