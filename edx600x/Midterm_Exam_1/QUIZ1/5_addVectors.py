def addVectors(v1, v2):
    """assumes v1 and v2 are lists of ints.
    Returns a list containing the pointwise sum of
    the elements in v1 and v2. For example,
    addVectors([4,5], [1,2,3]) returns [5,7,3],and
    addVectors([], []) returns []. Does not modify inputs."""
    if len(v1) > len(v2):
        result = v1[:]
        other = v2[:]
    else:
        result = v2[:]
        other = v1[:]
    for i in range(len(other)):
        result[i] += other[i]
    return result

v1 = [4, 5]
v2 = [1, 2, 3]

print addVectors(v1, v2)
print v1
print v2