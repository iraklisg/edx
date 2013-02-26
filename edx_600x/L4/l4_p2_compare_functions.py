def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(x, y):
    return a(x>y, x, y)
     
#b=a(-1,4,5)
#print b

print a(a>b, a, b)
print b(a, b)