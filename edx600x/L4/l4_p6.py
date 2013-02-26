x = 12
def g(x):
  x = x + 1
  def h(y):
      return x + y
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