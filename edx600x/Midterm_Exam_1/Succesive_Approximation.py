# lecture 3.5, slide 2

x = 0.2
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
print "ans before loop is ",ans
while (abs(ans**2 - x)) >= epsilon and ans <= x and numGuesses <=2555555:
    print 'ans = ',ans,'and (ans^2-x) = ',abs(ans**2 - x)
    ans += step
    numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))
    
# lecture 3.6, slide 2
# bisection search for square root

x = 12345
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))

# Lecture 3.7, slide 3

# Newton-Raphson for square root

epsilon = 0.01
y = 24.0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))