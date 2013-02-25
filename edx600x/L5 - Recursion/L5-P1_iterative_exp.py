def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    #define my state variables (i, result)
    result = 1.0 # initialize state variable "result"
    #state variable "exp" initialized by value given through function call with parameter
    while exp > 0:
        result *= base #update the value of state variable "result" iteratively
        exp -= 1 #update the value of state variable "i" iteratively
        counter +=1
    return result

x=3.2
y=0   
print iterPower(x,y)
print x**y