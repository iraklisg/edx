def search(L, e):
    def bSearch(L, e, low, high):
        if high == low: # i.e. list of lenght 1
            print 'A. the L[low] = ',L[low]
            return L[low] == e
        mid = low + int((high - low)/2)
        print 'B. the mid = %s and L[mid] = %s'%(mid, L[mid])
        if L[mid] == e:
            print 'E. i found it ',L[mid]
            return True
        if L[mid] > e:
            print 'C. new high = %s and recursion input is %s '%(mid - 1, L[low:mid-1])
            return bSearch(L, e, low, mid - 1)
        else:
            print 'D. new low = %s and recursion input is %s '%(mid + 1, L[mid+1:high])
            return bSearch(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        print 'X. initial max = len(L)-1 =',len(L)-1
        return bSearch(L, e, 0, len(L) - 1) #low = 0 , high = Len(L)-1
    

def rBinarySearch(list, element):
    if len(list) == 1:
        return object == list[0]
    mid = len(list)/2
    print 'mid =',mid
    if list[mid] > element:
        print 'list[mid] = %s and recursive call with input list[ : mid] = %s'%(list[mid], list[ : mid])
        return rBinarySearch( list[ : mid] , element )
    if list[mid] < element:
        print 'object =',element
        print 'list[mid] = %s and recursive call with input list[mid : ] = %s'%(list[mid], list[mid : ])
        return rBinarySearch( list[mid : ] , element)
    return True

list = [1,2,3,4,5,6,7,8,9,10]
element = 10

print rBinarySearch(list,element)

#L = [1,2,3,4,5,6,7,8,9,10]
#print 'len(l) =',len(L)
#print L
#e = 10
#print search(L, e)