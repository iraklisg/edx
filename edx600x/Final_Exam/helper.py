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