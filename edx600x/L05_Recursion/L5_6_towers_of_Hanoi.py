def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

#suppose source is the 1st tower, destination is the 3rd tower and temp is the 2nd tower
#suppose n is the number of disks
#recursive solution: take n-1 disks and move them to the temp
#then take the Nth disk and move it to destination
#finaly move the stack of n-1 disks from temp to destination
def Towers(n, fr, to, spare):
    if n == 1:
        print '[``````````````]'
        printMove(fr, to)
        print '[,,,,,,,,,,,,,,,]'
        
    else:
        print '1st step, value of n=',n
        Towers(n-1, fr, spare, to)
        print '2nd step, value of n=',n
        Towers(1, fr, to, spare)
        print '3rd step, value of n=',n
        Towers(n-1, spare, to, fr)

Towers(3, '1', '3', '2')