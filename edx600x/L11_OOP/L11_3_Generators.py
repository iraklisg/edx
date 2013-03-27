def genTest():
    yield 1
    a = 2+3
    yield a
    b = 666
    print 'hihi'

print genTest()
a = genTest() # `a` is now a generator object that derived from genTest() generator. `a` generator objecthas a next() method
print a.next() # starts executing procedure upon and including the 1st yield statement
print a.next() # resumes executing procedure from after previous yield and upon and including the next yield statement
#UNCOMENT THE FOLLOWING LINE
# print a.next() # resumes executing procedure from after previous yield; If I reach the end of generator procedure and meet no other yield,
                # I return from generator and raises a StopIteration exception
'''FOR loop and GENERATORS'''                
for n in genTest():
    print n
    
def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        ans = fibn_1 + fibn_2
        yield ans
        fibn_2 = fibn_1
        fibn_1 = ans
        # yield statement is inide an infinite while loop, so neve3r returns and never raises a StopIteration exception
        # by succesivley calling next() I keep on ubdating fibn_2 and fibn_1 and then producing the next ans = fibn_1 + fibn_2
        
#UNCOMENT THE (2) FOLLOWING LINEs
# for i in genFib(): # i will take the value of the yield statement, i.e. ans
#     print i

''' return a genarator instead of a list which I'm going to use to itterate over its elements'''
def foo1():
    lista = [1, 2, 3, 4, 5]
    return lista[:]

print foo1() # return a copy of list

def foo2():
    lista = [1, 2, 3, 4, 5]
    for e in lista:
        yield e

print foo2() # returns a generator object

for i in foo1():
    print i # I have created a copy of lista and now I iterate over its elements

for i in foo2():
    print i # I return on-the-fly, one-by-one the elements of lista