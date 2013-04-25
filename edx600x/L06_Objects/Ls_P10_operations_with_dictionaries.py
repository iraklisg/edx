def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    my_list = aDict.values() 
    my_flattened_list = [i for sublist in my_list for i in sublist] # list comprehension - flattening...
    # ...give my all elements "i" gia kathe sublist sthn lista mou kai gia kathe i stin kathe sub lista
    return len(my_flattened_list)
# single line code: return len([i for sublist in aDict.values() for i in sublist])
        
        




animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print howMany(animals)