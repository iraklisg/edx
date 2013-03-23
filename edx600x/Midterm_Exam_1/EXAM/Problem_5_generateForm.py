def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    # Your Code Here
    initial_story = story.split() # list form of the initial story
    madlib_story = [] # list form of the mad-lib story
    for word in initial_story:
        if word in listOfAdjs:
            madlib_story.append('[ADJ]')
        elif word in listOfNouns:
            madlib_story.append('[NOUN]')
        elif word in listOfVerbs:
            madlib_story.append('[VERB]')
        else:
            madlib_story.append(word)
    return ' '.join(madlib_story)

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    # Your Code Here
    madlib_form = madLibsForm.split()
    mad_template = [] # this will be finally returned
    for e in madlib_form:
        if e in ['[ADJ]', '[VERB]', '[NOUN]']:
            mad_template.append(e)
    return mad_template
                
def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    # Your Code Here
    if madTemplate == '[ADJ]':
        return userWord in listOfAdjs
    elif madTemplate == '[NOUN]':
        return userWord in listOfNouns
    else:
        return userWord in listOfVerbs



story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']

madLibsForm = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
print madLibsForm
print 'At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear'
print generateTemplates(madLibsForm)
userWord = 'plaid'
madTemplate = '[ADJ]'
print verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs)