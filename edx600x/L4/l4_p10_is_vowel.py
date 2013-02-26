def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
#    if char=='a'or char=='A' or char=='e' or char=='E'or char=='i' or char=='I' or char=='o' or char=='O' or char=='u'or char=='U':
#        return True
#    else:
#        return False
#
#print isVowel('U')

#    vowels = 'aeiouAEIOU'
#    i=0
#    print('len = '+str(len(vowels)))
#    while i<len(vowels):
#        if char == vowels[i]:
#            ans=1
#        else:
#            ans = 0
#        i+=1
#    print('i =',i)  
#    return bool(ans)


    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False

print isVowel('f')

