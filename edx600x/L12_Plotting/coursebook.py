##import numpy
#import pylab
#
#
#a = [10,20,30,40]
##print a
##b = a + 1 #TypeError: can only concatenate list (not "int") to list
##print b
#
#x = pylab.array(a)
#print x
#print type(x)
#y = x + 1
#print y
#pylab.figure(1)
#pylab.plot([1,2,3,4], [1,7,3,5])
#pylab.figure(2)
#pylab.plot(a)
#pylab.close()
##pylab.show()
#print 'ante kai gamisou'
#
#
#
#a = "abcd"
#print a[0]

import numpy as np  
from pylab import *      
n = 256  
X = np.linspace(-np.pi,np.pi,n,endpoint=True)  
Y = np.sin(2*X)  

plot (X, Y+1, color='blue', alpha=1.00)  
plot (X, Y-1, color='blue', alpha=1.00)
show()