def program1(L):
    counter = 0
    multiples = []
    for x in L:
        counter +=1 #+1 step for every iteration of outer loop for check True/False
        print 'outer loop runs',counter
        for y in L:
            multiples.append(x*y)
            counter +=2 #+3 steps for every iteration of inner loop (1 step for check, 1 step for multiplication plus 1 step for appending)
            print 'inner loop runs',counter
    return multiples

L = [2,3,5] #n-elements , n=2
program1(L) # 1 step for multiples assign. + n(3*n+1) for nested loop + 1 for return
#_Explanation of n*(3*n+1) for nested loop_:
#outer loop runs n times, and each time execute  1 step for x in L + inner loop, i.e. n * (1step for x in L check + inner loop) (I)
#inner loop runs n time each time performs 1 step for y in L check + 2steps for .append(x*y), i.e. n*3 (II)
#Therefore, total running time for nested loop from (I),(II)is n * (1 + (3*n)) = n*(3*n+1)

def program3(L1, L2):
    intersection = []
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection

#1 step for assign intersection and 1 step for return, =total 2 (I)
# outer loop runs n times, each time performing:
#    1 step for check
#    n steps in worst case scenario assuming that elt found in L2 is True in the n-th element of L2
#   1 step for append
#Hence, outer loop performs n * (1+(n+1)) = n*(n+2)