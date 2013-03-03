'''done with recursion: I should check it again and if possible reduce base cases and recurive cases from 2+2 to 1+1
since recursive_case_1 is base_case_1 + recursive_step
'''
#def getGuessedWord(secretWord, lettersGuessed):
#    '''
#    secretWord: string, the word the user is guessing
#    lettersGuessed: list, what letters have been guessed so far
#    returns: string, comprised of letters and underscores that represents
#      what letters in secretWord have been guessed so far.
#    '''
#    # FILL IN YOUR CODE HERE...
#    if     len(secretWord) <= 1 and secretWord[0] in lettersGuessed:
#        return secretWord[0]
#    elif len(secretWord) <= 1 and secretWord[0] not in lettersGuessed:
#        return " _ "
#    elif secretWord[0] in lettersGuessed:
#        return secretWord[0] + getGuessedWord(secretWord[1:], lettersGuessed)
#    else:
#        return " _ " + getGuessedWord(secretWord[1:], lettersGuessed)
'''done with list comprehension
'''
def getGuessedWord(secretWord, lettersGuessed): 
    return "".join([i if i in lettersGuessed else " _ " for i in secretWord ]) # list comprehension
    

   
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
secretWord = 'applex'
print 'start'
print(getGuessedWord(secretWord, lettersGuessed))