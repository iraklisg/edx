#PROBLEM 4 : 8.0 POINTS
#The procedure isMyNumber is used to hide a secret number (integer). It takes an integer x as a parameter and compares it to the secret number. It returns:
#-1 if the parameter x is less than the secret number
#0 if the parameter x is correct
#1 if the parameter x is greater than the secret number
def isMyNumber(guess):
    secret = 2
    if guess < secret:
        return -1
    elif guess > secret:
        return 1
    else:
        return 0

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 0
#    if isMyNumber(guess) == 0:
#        return guess
#    foundNumber = False
    while True:
        sign = isMyNumber(guess)
        if sign == -1:
            guess += 1
        elif sign == 1:
            guess -= 1
        else:
            return guess
#            foundNumber = True
#    return guess
print jumpAndBackpedal(isMyNumber)