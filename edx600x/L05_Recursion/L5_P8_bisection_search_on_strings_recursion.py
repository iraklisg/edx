def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # BASE CASES
    length = len(aStr)
    if length == 0:
        print 'length 0'
        return False
    elif length == 1:
        print 'length 1'
        return char == aStr
    #recursive case
    elif length > 1:
        if char == aStr[length/2]:
            return True
        elif char > aStr[length/2]:
            print '<IRA> compare char '+char+' with mid character '+aStr[len(aStr)/2]+ ' in1: '+aStr+' and return ' + aStr[len(aStr)/2:]
            return isIn(char, aStr[length/2:])
        elif char < aStr[length/2]:
            print '<IRA> compare char '+char+' with mid character '+aStr[len(aStr)/2]+ ' in2: '+aStr+' and return ' + aStr[:len(aStr)/2]
            return isIn(char, aStr[:length/2])
def isInn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr=='':
        print 'length 0'
        return False
    elif len(aStr)==1:
        if char==aStr:
            print 'length 1a'
            return True
        else:
            print 'length 1b'
            return False
    elif char==aStr[len(aStr)/2]:
        return True
    elif char>aStr[len(aStr)/2]:
        print '<NICK> compare char '+char+' with mid character '+aStr[len(aStr)/2]+ ' in1: '+aStr+' and return ' + aStr[len(aStr)/2:]
        return isInn(char,aStr[len(aStr)/2:])
    else: #char<aStr[len(aStr)/2]:
        print '<NICK> compare char '+char+' with mid character '+aStr[len(aStr)/2]+ ' in2: '+aStr+' and return ' + aStr[:len(aStr)/2]
        return isInn(char,aStr[:len(aStr)/2])
    
def isInnn(char, aStr):
    if aStr=="":
        print 'length 0'
        print False
    else:
        n=len(aStr)
        if char==aStr[n/2]:
            print True
        elif char>aStr[n/2]:
            print '<MITSOS> compare char '+char+' with mid character '+aStr[len(aStr)/2]+ ' in1: '+aStr+' and return ' + aStr[len(aStr)/2+1:]
            return isInnn(char,(aStr[(n/2)+1:]))
        else:
            print '<MITSOS> compare char '+char+' with mid character '+aStr[len(aStr)/2]+ ' in2: '+aStr+' and return ' + aStr[:len(aStr)/2]
            return isInnn(char,(aStr[:(n/2)]))

stingaki = 'abcdefghij'
print len(stingaki)
print isIn('j', stingaki)
print isInn('j', stingaki)
print isInnn('j', stingaki)

#"The operator [n:m] returns the part of the string from the n-eth character to the m-eth character, including the first but excluding the last"

        