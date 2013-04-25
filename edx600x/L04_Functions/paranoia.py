
def make_adder(n):
    def add(x):
        return x + n

    return add

add_five = make_adder(5)
#add_five pairnei tin timi tis make_adder(5)
#h make_adder epistrefei thn add()!!! Ara h add_five pairnei gia timi
# tin add <type=function> me opou n=5 dhladh h add_five einai nea sinartisi!!!!
#to anaptygma tis add_five pleon einai:
#add_five(k):
#    return k+5


print add_five
print add_five(2) 

"================================================================="
x = 12
def gg(x):
  x = x + 1
  def h(y):
      return x + y # 1st looks for the value of x einai environment E2 that the call of h(y) has initialized
  #if not it looks in the previous "parent" environment (stack frame) where the h(x) was called
  #if not it looks at the previous Environment, that is the Gobal Environment
  return h(6)
z=gg(x)
print z 

"================================================================="
#prosoxh kanei mono inherit! den paei stoyu idiou epipedou ta environments para mono sto mpampa h ston idio h sgto papou
x = 12
a=30
def g(x):
    a=20
    x = x + 1
    def h(y):
        a=10
        b=4
        return a + y #takes the value of a from E2 if not from E1 if not from Global Environment
    def k():
        return b #error because cannot search in same-level environment
        
    return h(6)
z=g(x)
print z 
"================================================================="
#x=44
def foo (x):
#    x=55
    def bar (z):
#        x=100
        return z + x
    return bar(3)

foo(2)
print 'foo = ',foo(2)

