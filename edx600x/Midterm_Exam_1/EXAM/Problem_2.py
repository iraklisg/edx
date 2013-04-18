def upAndDown(n):
    if n == 0:  return 
    if n == 1:  return 
    if n%2 == 0:
        return upAndDown( n/2 )
    if n%2 == 1:
        return upAndDown( n*3 + 1 )
    return "All Done"