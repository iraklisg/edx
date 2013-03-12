def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L): # j loops from the element next of element minVal=L[i] through the end of the list
            if minVal > L[j]: # if I found an element L[j] > minVal
                minIndx = j #then set minIndx = j
                minVal= L[j] # and set minVal = L[j] i.e. the value of that element
            j += 1
        # I swap L[i] with L[minIndx]. That is:
        # ...I set variable temp to be equal to L[i] 
        temp = L[i]
        # ...I swap the value of L[i] with L[j] , where j is the index of the element with the smallest value compared to L[i]
        
        L[i] = L[minIndx]
        # ...I swap the L[j] , j is the index with the min value I found with L[i]
        L[minIndx] = temp