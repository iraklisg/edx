def search(L, e):
    def bSearch(L, e, low, high):
        if high == low: # i.e. list of lenght 1
            print 'A. the L[low] = ',L[low]
            return L[low] == e
        mid = low + int((high - low)/2)
        print 'B. mid= %s and L[mid]= %d'%(mid, L[mid])
        if L[mid] == e:
            print 'E. i found it ',L[mid]
            return True
        if L[mid] > e:
            print 'C. Same low=%d, New high=%d '%(L[low], L[mid - 1])
            return bSearch(L, e, low, mid - 1)
        else:
            print 'D. New low=%d, Same high=%d '%(L[mid + 1], L[high])
            return bSearch(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        print 'X. initial max = len(L)-1 =',len(L)-1
        return bSearch(L, e, 0, len(L) - 1) #low = 0 , high = Len(L)-1


L = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print 'len(l) =',len(L),'\n'
print L
print ' |  |  |  |   |    |   |    |    |    |'
print '[0  1  2  3   4    5   6    7    8    9]\n'
e = 16
print 'Looking for value ***%d***\n'  %e
print search(L, e)
