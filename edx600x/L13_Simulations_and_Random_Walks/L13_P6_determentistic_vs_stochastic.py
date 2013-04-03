import random
mylist = []

for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        print number
        mylist.append(number)
print mylist
