def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    return "".join([i for i in string.ascii_lowercase if i not in lettersGuessed])


print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])