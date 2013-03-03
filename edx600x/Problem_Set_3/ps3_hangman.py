# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    return "".join([i if i in lettersGuessed else " _ " for i in secretWord ]) # list comprehension


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return "".join([i for i in string.ascii_lowercase if i not in lettersGuessed])
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = [] # initialization of list containing the letters guessed so far
    availableLetters = getAvailableLetters(lettersGuessed)
    mistakesMade = 0
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %s letters long.' %(len(secretWord))
    print '-------------'
    counter = 8
    while True:
        print 'You have %s guesses left.'%(counter)
        print "Available letters:", getAvailableLetters(lettersGuessed)
        guess = (raw_input('Please guess a letter: ').lower()) #the current letter guessed
        if guess not in availableLetters:
            print 'Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
        else:
            if guess in secretWord:
                lettersGuessed.append(guess)
                availableLetters = getAvailableLetters(lettersGuessed)
                print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
                print '-------------'
            else:
                lettersGuessed.append(guess)
                availableLetters = getAvailableLetters(lettersGuessed)
                print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
                counter -= 1
                mistakesMade += 1
                print '-------------'
            if mistakesMade == 8:
                print 'Sorry, you ran out of guesses. The word was %s.'%(secretWord)
                break
            if "_ " not in getGuessedWord(secretWord, lettersGuessed):
                print 'Congratulations, you won!'
                break               

                
                
                 
        
        
#
#You have 8 guesses left.
#    Available letters: bcdefghijklmnopqrstuvwxyz
#    Please guess a letter: s
#    Oops! That letter is not in my word: _ a_ _
#
#You have 8 guesses left.
#    Available letters: abcdefghijklmnopqrstuvwxyz
#    Please guess a letter: a
#    Good guess: _ a_ _




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'sea'
print secretWord
hangman(secretWord)

