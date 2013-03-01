def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)


def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')

print testFib(10)

def fibMeteredd(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMeteredd(x-1) + fibMeteredd(x-2)

def testFibb(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMeteredd(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFibb(10)