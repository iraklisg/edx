def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    #Identify the base case: s = 0
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])

print lenRecur('sdkfjh')
