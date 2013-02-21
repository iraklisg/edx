# lecture 3.5, slide 2

x = 0.25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
print "ans before loop is ",ans
while (abs(ans**2 - x)) >= epsilon and ans <= x and numGuesses <=500000:
    print 'ans = ',ans,'and (ans^2-x) = ',abs(ans**2 - x)
    ans += step
    numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))