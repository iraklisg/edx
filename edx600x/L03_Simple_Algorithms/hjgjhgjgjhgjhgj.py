#x = 12
#a=5
#def g(x):
#  x = x + 1
#  a=8
#  def h(y):
#      a=9
#      return a + y
#  return h(6)
#z=g(x)
#print z 


#prosoxh kanei mono inherit! den paei stoyu idiou epipedou ta environments para mono sto mpampa h ston idio h sgto papou
x = 12
def g(x):
    x = x + 1
    def h(y):
        return a + y
    def k():
        a=100
    return h(6)
z=g(x)
print z 


def make_adder(n):
    def add(x):
        return x + n

    return add

add_five = make_adder(5)
print add_five
print add_five(2) 