import random
def genEven():
    '''
    Generates a random number x, where 0 <= x < 100
    '''
    # Your code here
    # even number x: x%2 = 0
    x = int(random.uniform(0, 100))
    while x % 2 != 0:
        x = int(random.uniform(0, 100))
    return x

print genEven()
