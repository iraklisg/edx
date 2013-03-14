def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    #Base case
    if len(aStr) < 2:
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr

aStr = 'abcd'
print reverseString(aStr)