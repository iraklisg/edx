import itertools
def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    # Your Code Here
    # 5a+8b+24c=n
    range_c = n/24+1
    range_b = n/8+1
    range_a = n/5+1
    for c in range(range_c):
        for b in range(range_b):
            for a in range(range_a):
                res = 5*a + 8*b + 24*c
                print 'a = %s , b = %s, c = %s , res = %s'%(a,b,c,res)
                if res == n:
                    return True
                elif res > n:
                    print ' ==== start over ===='
                    break
    return False
    # empneusi!!!!
#    a = 5
#    b = 8
#    c = 24
#    ans = 1
#    for i in itertools.permutations([c,b,a],3):
#        print '%d _mod_ %s = %s'%(n, i[0], n%i[0])
#        print '%d _mod_ %s = %s'%(n%i[0], i[1], n%i[1])
#        print '%d _mod_ %s = %s'%(n%i[1], i[2], n%i[2])
#        ans *= ((n%i[0])%i[1])%i[2]
#        print ans 

#    #calculate mods
#    aa = n%a
#    bb = n%b
#    cc = n%c
#    # if mods are == 0 then a cobination of one of the 3 boxes can be the solution  
#    if n < a and (n%a == 0 or n%b == 0 or n%c == 0):
#        print 'case 1: n_mod_a = %s, n_mod_b = %s, n_mod_c = %s'%(n%a, n%b, n%c)
#        return True
#    else:
#        aa = n%a
#        bb = n%b
#        cc = n%c
#        return numPens(n%c)
    
    
    
#    elif  n%b == a: # since a xwraei ligotero apo 2 fores sto b [i.e.  n%b < 2* a]
#        print 'case 2: n_mod_a = %s, n_mod_b = %s, n_mod_c = %s'%(n%a, n%b, n%c)
#        return True
#    ###############################################################################
#    
#    elif n%c == a or n%c == b or n%c == a+b:
#        print 'case 3: n_mod_a = %s, n_mod_b = %s, n_mod_c = %s'%(n%a, n%b, n%c)
#        return True
#    else:
#        return False

print numPens(42)
        
        
        
