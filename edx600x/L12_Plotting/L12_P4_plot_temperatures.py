import pylab
a = [1, 2, 3, 4, 5]
b = [10, 20, 30,40, 50, 60]
#print a - b
x = pylab.array(a)
y = pylab.array(b)
print x
print y
print x -y
print type(x)
for e in x:
    print e