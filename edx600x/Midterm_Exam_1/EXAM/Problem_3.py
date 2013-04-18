## 3.1
stuff  = 'iPad'
for thing in stuff:
    print thing
    if thing == 'iPad':
        print "Found it"

## 3.2
# The following Python code is supposed to compute the square of an integer by using succesive additions.
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x