monthNumbers = { 'Jan':1, 'Feb':2, 'Mar':3, 1:'Jan',2:'Feb', 3:'Mar'}
print(monthNumbers['Jan'])
monthNumberss = { 'Jan':1, 'Feb':2, 'Mar':3}
print "with value as an argument", monthNumbers[1]
print "with key as an argument", monthNumbers['Feb']

#Insertion
#associated with the key 'Apr' as a string I want to give the value 4
monthNumberss['Apr'] = 4
print monthNumberss 

#Iteration
list = []
for i in monthNumberss:
    list.append(i)
print list    # it will put the *keys* in a list

#Comparison
print monthNumberss.keys()