import operator
def merge(left, right, compare):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle], compare)
        print 'left',left
        right = mergeSort(L[middle:], compare)
        print 'right',right
    return merge(left, right, compare)

L = [9, 8, 7, 6, 5, 4, 3]
mergeSort(L)