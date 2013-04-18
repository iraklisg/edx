counter_i = 0
counter_j = 0
counter_k = 0
for i in range(10):
    print 'i =',i
    counter_i += 1
#    print 'counter_i =',counter_i
    if i > 3:
        print '======= i BREAK ======'
        break
    for j in range(10):
        print '    j =',j
        counter_j += 1
#        print 'counter_j =',counter_j
        if j+i > 4:
            print '======= j BREAK ======'
            break
        for k in range(10):
            print '        k =',k
            counter_k += 1
#            print 'counter_k =',counter_k 
            if i+j+k > 5:
                print 'i = %s, j = %s, k = %s'%(i,j,k)
#                print 'counter : i = %s, j = %s, k = %s'%(counter_i, counter_j, counter_k)
                print ' ====== k BREAK ======  i+j+k =', i+j+k
                break # SOS!!! after break, outer loop j ++ and k restarts from 0 again