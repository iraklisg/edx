import numpy
import pylab

inFile = open('julyTemps.txt')
line = inFile.readline()
line = inFile.readline()
fields = line.split(" ")
if len(fields) < 3 or not fields[0].isdigit():
    print "malakia"
line = inFile.readline()
line = inFile.readline()
line = inFile.readline()
line = inFile.readline()
line = inFile.readline()
fields = line.split(" ")
print fields
if len(fields) < 3 or not fields[0].isdigit():
    print "malakia"