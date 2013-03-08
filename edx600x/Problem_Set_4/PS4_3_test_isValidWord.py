import operator
reduce(operator.mul, (3, 4, 5), 1)

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function

    ans = 1
    if word not in wordList:
        return False
    else:
        for i in word:
            if hand.has_key(i) == True and hand.get(i) > 0:
                ans *= 1
                hand[i] =   hand.get(i) - 1
            else:
                ans *= 0
                break
        return bool(ans)
        
           
    if word not in wordList:
        return False
    else:     
        return reduce(lambda x, y: x*y, [hand.has_key(i)*hand.get(i)>0 for i in word])
    


    
