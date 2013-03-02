def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if     len(secretWord) <= 1:
        print 'BASE CASE: check %s in %s and return %s'%(secretWord[0], lettersGuessed, secretWord[0] in lettersGuessed) 
        return secretWord[0] in lettersGuessed
    else:
        print 'RECURSIVE CASE: check %s in %s and return %s'%(secretWord[0], lettersGuessed, secretWord[1:]) 
        #print 'RECURSIVE CASE: check %s in %s and return %s, and remains %s'%(secretWord[0], lettersGuessed, isWordGuessed(lettersGuessed, secretWord[1:]) and (secretWord[0] in lettersGuessed), secretWord[1:]) 
        return (secretWord[0] in lettersGuessed) and isWordGuessed(secretWord[1:], lettersGuessed) 

   
lettersGuessed = ['a', 'e', 'l','x', 'p', 'p']
secretWord = 'apple'
print 'start'
print(isWordGuessed(secretWord, lettersGuessed))

#def fun(L, secret_word):
#    length = len(L)
#    if     length <= 1:
#        return L[0] in secret_word
#    else:
#        return (L[0] in secret_word) and fun(L[1:], secret_word)
#
#   
#L = ['x', 'a', 'e', 'l', 'p', 'p' ]
#secret_word = 'apple'
#print(fun(L, secret_word))