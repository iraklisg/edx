def recur(x, y, type = 0, rem = 0):
    if x == 0 or y == 0:
        return type
    elif x == 0 and y == 0:
        return rem
    else:
        print 'type = ',type
        print 'rem = ',rem
        recur(x-1, y-1, type+1, rem+1)
        return (type, rem)


print recur(6, 5)

for i in range(1, 10+1, 3):
    print i

# XOR
print set([1,2,3,8,9]) ^ set([4,7,2,1,3])

#recursion with list
def recur1(num, arr = []):
    
    if num == 0:
        return arr
    else:
        return recur1(num-1, [num] + arr) # concatenate arr+num

print recur1(4)