'''
Created on Feb 21, 2013

@author: ira
'''
def square(x):
    '''
    x: int or float.
    '''
    return x*x

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(x)*square(x)

print fourthPower(5)