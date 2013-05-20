#def f(x):
#    import math
#    return 10*math.e**(math.log(0.5)/5.27 * x)

def f(x):
    import math
    return 200*math.e**(math.log(0.5)/14.1 * x)

#def f(x):
#    return 20

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    if start >= stop-step:
        print 'START =',start
        print 'F(START) =', f(start) 
        return f(start) * step
    else:
        print 'start =',start
        print 'f(start) =', f(start) 
        return (f(start) * step) + radiationExposure(start+step, stop, step)
    
print radiationExposure(0, 3, 0.1)

#start = 1
#end = 10
#step = 0.5
#count = 0
#while start < end:
#    print start
#    start += step
#    count += 1
#print count


