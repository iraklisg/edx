def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO
#    if len(x) < 2:
#        return x in word
#    elif len(x) >=2 and x[0] in word: 
#        j = word.index(x[0])
#        return x_ian(x[1:], word[j+1:])
#    else:
#        return False
    #BASE CASE: x is of length 0 or 1, return true/false according to if x is in word
    if len(x) < 2:
        return x in word
    #RECURSIVE CASE: x is 
    elif len(x) >=2 and x[0] in word: 
        j = word.index(x[0])
        return x_ian(x[1:], word[j+1:])
    else:
        return False



print x_ian('eric', 'electronic')
