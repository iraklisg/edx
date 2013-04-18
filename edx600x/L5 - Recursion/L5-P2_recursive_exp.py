def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    
    '''
    if exp == 0: #base case
        return 1
    else:
        #recursive case base^exp = base*base^(exp-1)
        return base * recurPower(base, exp-1)
print recurPower(3,4)