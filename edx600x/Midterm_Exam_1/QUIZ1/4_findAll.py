def findAll(wordList, lStr):
    """
    assumes:    wordList is a list of words in lowercase.
                lStr is a str of lowercase letters.
                No letter occurs in lStr more than once
    returns:    a list of all the words in wordList that contain
                each of the letters in lStr exactly once and no
                letters not in lStr.
    
    """
    newList = []
    for word in wordList:
        flag = True
#        print 'now I am checking word "%s"'%(word)
        for letter in word:
#            print 'now I am checking letter "%s" of word "%s"'%(letter, word)
            if letter not in lStr:
#                print 'letter "%s" not in "%s"'%(letter, lStr)
                flag = False
                break
#        print 'flag = ',flag
        if flag == True:
            newList.append(word)
    return newList

# "Pythonic" solution: Using list comprehension [x for b in a for x in b]
#    return [word for word in wordList if lStr.find(word) != -1]    



wordList = ['nick', 'mitsos', 'ira', 'panos']
lStr = 'irapson'
print findAll(wordList, lStr)
                
    