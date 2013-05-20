# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    uppercase_letters = string.ascii_uppercase # A string that contains all uppercase letters in order
    lowercase_letters = string.ascii_lowercase # A string that contains all lowercase letters in order
    length_upper = len(uppercase_letters)
    length_lower = len(lowercase_letters)
    # create uppercase cipher {key:value} such as dict = {string[i]:string[i+shift] if i < len(string)-shift else string[i+shift-len(string)] for i in range(len(string))}
    # In general, dict comprehension: {(some_key if some_condition==True else other_key) : (some_value if some_condition==True else other_value), for some_range_of_values }
    # Example 1: { (some_key if condition else default_key):(something_if_true if condition else something_if_false) for key, value in dict_.items() }
    # Example 2: { (some_string[i] if i > 10 else some_string[i+1]):(some_other_string[i] if i > 5 else some_other_string[i+1]) for i in some_range }  
    # Example 3: d is a {key:some_dictionary.get(key, 0) for key in some_range}
    dict_upper = {uppercase_letters[i] : uppercase_letters[i+shift] if i < length_upper-shift else uppercase_letters[i+shift-length_upper]  for i in range(length_upper)}
    # create lowercase cipher
    dict_lower = {lowercase_letters[i] : lowercase_letters[i+shift] if i < length_lower-shift else lowercase_letters[i+shift-length_lower]  for i in range(length_lower)}
    # Built cipher dictionary by merging dict_upper and dict_lower:
    # In general: merge dictionaries x, y into dictionary z : z = dict(x.items() + y.items())
    cipher = dict(dict_upper.items() + dict_lower.items())
    return cipher

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    ciphertext = "" #initialize ciphertex
    for i in text:
        ciphertext += str(coder.get(i, i))
    return ciphertext

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
#    cipher = buildCoder(shift)
#    ciphertext = applyCoder(text, cipher)
#    return ciphertext
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    #For every possible cipher key : [0, 25] (3)
    number_of_actual_words_so_far = 0
    best_key = 25
    for key in range(26):
    #   decipher text using applyShift(text, 26-shift)
        plaintext = applyShift(text, 25-key)        
    #   Break deciphered text in a list of deciphered words using  " " as separator
        plaintext_list = plaintext.split(' ')
    #   for every word in the list of deciphered words
        number_of_current_actual_words = 0
        for word in plaintext_list:
    #        check if this word is an actual word (i.e. is comprised in wordList) using isWord(wordList, word)
            if isWord(wordList, word):
    #            if True: increase the current number_of_actual_words flag by 1
                number_of_current_actual_words += 1
    #   If the number_of_actual_words is more than the largest number of actual words found so far, then:
        if number_of_current_actual_words > number_of_actual_words_so_far:
            number_of_actual_words_so_far = number_of_current_actual_words
    #            update the best_shift to the current key
            best_key = 25-key 
    # Finally return the best shift
    return best_key

print findBestShift(loadWords(), "Nby nyuwbyl'm huGY cm Nuvcnbu?") # 6