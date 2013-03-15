def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO
    #BASE CASE: My text is < lineLength or I reached the end of text (no other spaces remaining after lineLength)
    if len(text) < lineLength or text[lineLength:].find(' ') == -1:
        return text
    #RECURSIVE CASE: My text is > lineLength and I have not reached the end of text (there are still more words)
    else:
        #try and find the next space after the lineLength-1 element
        j = text[lineLength-1:].find(' ')
        #concatenate the text up to that point (space) with a new line and the result of the recursive call with the remaining text 
        return text[:lineLength+j] + '\n' + insertNewlines(text[lineLength+j:], lineLength)
    
#    #BASE CASE: If the length of the text is smaller of the lineLength, return the text
#    if len(text) <= lineLength:
#        return text
#    #RECURSIVE CASE: If the length of the text is bigger than the linelength I should reduce the size of the text to fit lineLength
#    elif len(text) > lineLength:
#        #If the lineLength-th element is " "
#        if text[lineLength-1] == " ":
#            # concatenate the text up to and including the lineLength-th element with \n and with the the result of the recursive call of the rest of the text text[lineLegth :]
#            return text[:lineLength] + '\n' + insertNewlines(text[lineLength:], lineLength)
#        # Else, if the lineLength-th element != " ", i.e. i'm on the midle of a word
#        else:
#            # Try to find the index of the space character that follows that lineLength-th element 
#            j = text[lineLength:].find(" ")
#            # If there is no space, means I reached the end of string, so I return the whole text
#            if j == -1: #means there are no extra spaces, so text is the final remaining string
#                return text
#            # else I concatenate the text up to this point (lineLength+j) with /n and the result of the recursive call with the remaining string
#            else:             
#                return text[:(lineLength+j)] + '\n' + insertNewlines(text[lineLength+j+1:], lineLength)
 
            
text = 'Random text to wrap again.'
lineLength = 5
#arr = text.split()
#print arr
#print " ".join(arr)
print insertNewlines(text, lineLength)