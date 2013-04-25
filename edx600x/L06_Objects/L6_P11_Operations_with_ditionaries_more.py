def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
# STEP 1: identify what is the largest number of values a single key is associated with
    biggest_keys = []
    if aDict == {}:
        return None
    else:
        biggest_value = max([len(e) for e in aDict.values()]) #return a list with the max number of values associated with a key
# STEP 2: 
    for k, v in aDict.iteritems(): # i takes the values of keys!!!! not the values of values!!!
#        print 'key is %s and value is %s'%(k,v)
#        print 'key is '
        if len(v) == biggest_value:
            biggest_keys.append(k)
    return "".join(biggest_keys) # wants string for output, not list, thus I will convert list to string with "".join(list)
#single line solution!!!!!!
#[k for k,v in animals.iteritems() if len(v) == max([len(e) for e in animals.values()])]



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print biggest(animals)

print animals