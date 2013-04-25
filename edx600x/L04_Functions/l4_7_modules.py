import circle

#print pi # this does not work
print circle.pi
pi=0
circle.pi=100
print circle.area(2)

#pi=100
#print pi 
#from circle import *
#
#print pi # this does not work
#
#pi=100 # cannot overwrite!!!
#print area(2)