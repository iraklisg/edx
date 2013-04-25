import string
f ="lalala"
print list(f)
print f.split(" ")
print [x for x in f]

'''changing collection while iterating over elements'''

'''remove an element'''
elems  =  ['a',  'b',  'c']
for  e  in  elems:
    print  e
    elems.remove(e)

print 'A',elems # MISSING element b

# when  you  remove  the  'a' from  elems,  the  remaining  elements  slide
# down  the  list.  The  list  is  now  ['b',  'c'].  Now  'b'  is  at
# index  0,  and  'c'  is  at  index  1.  Since  the  next  iteration  is  going
# to  look  at  index  1  (which  is  the 'c'  element),  the  'b'  gets
# skipped  entirely!  

elems  =  ['a',  'b',  'c']
elems_copy  =  elems[:]
for  item  in  elems_copy:
        elems.remove(item)
print 'B',elems


''' append an element'''
# elems  =  ['a',  'b',  'c']
# for  e  in  elems:
#         print  e
#         elems.append(e)
# print 'C',elems # results in an infinite loop!!! 
elems  =  ['a',  'b',  'c']
elems_copy  =  []
for  item  in  elems:
        elems_copy.append(item)
print 'D',elems_copy

elems  =  ['a',  'b',  'c']
elems_copy  =  elems[:]
for  item  in  elems_copy:
        elems.append(item)
print 'E',elems