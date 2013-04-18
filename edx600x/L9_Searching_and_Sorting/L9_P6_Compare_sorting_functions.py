def mySort(L):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            print 'L[%d] is %s and L[%d] is %s'%(j-1, L[j-1], j, L[j])
            if L[j-1] > L[j]:
                clear = False # start scanning the list from the begining, if found L[j] < L[j-1] then clear = false and run again for loop from the begining
                temp = L[j]
                print 'temp = ',temp
                L[j] = L[j-1]
                L[j-1] = temp
                #if everything is sorted then if is not executed => clear = True => no need to run for loop again => I'm done !

L = [3, 7, 1, 4, 9, 5, 2]
mySort(L)