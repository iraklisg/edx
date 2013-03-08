import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
#    if len(word) == n:
#        return 50 + len(word) * sum([SCRABBLE_LETTER_VALUES[i] for i in word]) # for each i in word return the corresponding value from SCRABBLE_LETTER_VALUES[i]
#    return len(word) * sum([SCRABBLE_LETTER_VALUES[i] for i in word])

# ALTERNATIVE CODE
# I sum the elements of [SCRABBLE_LETTER_VALUES[i] for i in word] if len(word) != 0 , else if len(word) == n then I sum flattened list [50, mylist], i.e. I add 50 since sum() needs itterable item as argument like lists.  
    print sum(len(word)*[SCRABBLE_LETTER_VALUES[i] for i in word] if len(word) != n else [50] + len(word)*[SCRABBLE_LETTER_VALUES[i] for i in word])    


# ALTERNATIVE CODE    
#    ans = 0
#    word_length = len(word)
#    if word == "":
#        return 0
#    else:
#        for i in word:
#            ans += SCRABBLE_LETTER_VALUES[i]
#        if word_length == n:
#            return ans * word_length + 50
#        else:
#            return ans * word_length

#LIST COMPREHENSION
#  [v for k,v in SCRABBLE_LETTER_VALUES.items() if k in word] # ATTENTION: does not count the double characters in word !!!!
            
print getWordScore("it", 2) 
