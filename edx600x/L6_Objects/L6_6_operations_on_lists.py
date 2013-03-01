#methods applied to lists performing mutation (sort, insert, remove, append etc...) return None [NoneType]
#methods applied to lists not performing mutation (index, count etc...) return the corresponding value
#pop method performs mutation BUT returns the value
#methods that cannot be applied (e.g. remove an element that does not exist) return error
listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

print listA.sort()
print listA.insert(0, 100)
print listA.remove(1)

l= [100, 0, 1, 4, 4, 1, 6, 3, 4]
print l.pop(4)
print l
print l.reverse()
print l

listA = [100, 0, 1, 4, 7] 

listA.extend([4, 1, 6, 3, 4])
print listA
print listA.count(4)
print listA.index(1)
print listA.pop(4)
print listA.reverse()
print listA

