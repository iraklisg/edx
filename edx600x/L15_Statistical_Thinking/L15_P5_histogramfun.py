import pylab


WORDLIST_FILENAME = "words.txt"
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    ratio_vowels = []
    for word in wordList:
        wordlen = len(word)
        num_vowels = 0
        for letter in word:
            if letter in VOWELS:
                num_vowels +=1
        ratio_vowels.append(num_vowels / float(wordlen))
    #plot the histogram
    pylab.title('Proportion of vowels in each word in wordList')
    pylab.xlabel('Proportion of vowels per word')
    pylab.ylabel('Number of words')
    x_min, x_max = pylab.xlim()
    pylab.xticks(pylab.linspace(int(x_min), int(x_max), 11))
    pylab.hist(ratio_vowels, numBins)
    
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
    pylab.show()
