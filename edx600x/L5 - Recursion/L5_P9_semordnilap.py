def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    
    '''
    #base case
    if len(str1) != len(str2):
        return False
    if len(str1) == 1: #antistica o nikos to theorise gia str1 ="" einai to base case mou:an den to valw tote molis kata to 
        #recursive call ellatothei to str1,str2 se = "", tha paei na ksanakalesei to recursive call
        #kai tote string index out of range!. Einai gia na tou pw where to stop!!!!!
        return str1[0] == str2[-1]
    else:
        print 'first char of current str1[0]=',str1[0]
        print 'last char of current str2[-1]=',str2[-1]
        print 'str1=',str1[1:]
        print 'str2=',str2[:-1]
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])

#def semordnilap(str1, str2):
#    '''
#    str1: a string
#    str2: a string
#    
#    returns: True if str1 and str2 are semordnilap;
#             False otherwise.
#    '''
#    if len(str1)!=len(str2):
#        return False
#    if str1!='' and str2!='':
#        if str1[0]==str2[-1]:
#            print 'Sygkrisi: ' + str1[0]+ '=' + str2[-1]
#            return semordnilap(str1[1:],str2[:-1])
#        else:
#            return False
#    return True
s1 = 'desrerts'
s2 = 'stressed'
print semordnilapWrapper(s1, s2)
print 'goodbye world!'