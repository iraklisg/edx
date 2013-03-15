# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    #Base case
    if len(aStr) < 2:
        return aStr
    else:
        reverseString(aStr[0:-1]) + aStr

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.
    if len(x) < 2:
        return x in word
    elif len(x) >=2 and x[0] in word: 
        j = word.index(x[0])
        return x_ian(x[1:], word[j+1:])
    else:
        return False


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
        #BASE CASE: If the length of the text is smaller of the lineLength, return the text
    if len(text) <= lineLength:
        return text
    #RECURSIVE CASE: If the length of the text is bigger than the linelength I should reduce the size of the text to fit lineLength
    elif len(text) > lineLength:
        #If the lineLength-th element is " "
        if text[lineLength-1] == " ":
            # concatenate the text up to and including the lineLength-th element with \n and with the the result of the recursive call of the rest of the text text[lineLegth :]
            return text[:lineLength] + '\n' + insertNewlines(text[lineLength:], lineLength)
        # Else, if the lineLength-th element != " ", i.e. i'm on the midle of a word
        else:
            # Try to find the index of the space character that follows that lineLength-th element 
            j = text[lineLength:].find(" ")
            # If there is no space, means I reached the end of string, so I return the whole text
            if j == -1: #means there are no extra spaces, so text is the final remaining string
                return text
            # else I concatenate the text up to this point (lineLength+j) with /n and the result of the recursive call with the remaining string
            else:             
                return text[:(lineLength+j)] + '\n' + insertNewlines(text[lineLength+j+1:], lineLength)
