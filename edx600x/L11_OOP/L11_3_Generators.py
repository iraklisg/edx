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
# print a.next() # resumes executing procedure from after previous yield; If I reach the end of generator procedure and meet no other yield,
                # I return from generator and raises a StopIteration exception
print 'FOR loop and GENERATORS'                
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

for i in genFib(): # i will take the value of the yield statement, i.e. ans
    print i