monthNumbers = { 'Jan':1, 'Feb':2, 'Mar':3, 1:'Jan',2:'Feb', 3:'Mar'}
print(monthNumbers['Jan'])
monthNumberss = { 'Jan':1, 'Feb':2, 'Mar':3}
#print "with value as an argument result to error!!!!", monthNumberss[1] # key error!!!!!!!!!
print "with key as an argument", monthNumberss['Feb']

#Insertion
#associated with the key 'Apr' as a string I want to give the value 4
monthNumberss['Apr'] = 4
print monthNumberss 

#Iteration
my_list = []
for i in monthNumberss:
    my_list.append(i)
print my_list    # it will put the *keys* in a list

#Comparison
print monthNumberss.keys()

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
del animals['b']
print animals
print animals.values()