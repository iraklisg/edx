import math
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result #reminder of %10 basically pop out the last digit e.g. 12%10 = 2
        i = i/10 #devision with 10 basically shifts i to the right; then again at the begining of the loop I,m going to extract the bottom digit and so on, until the i/10 give me a result<1  
    return result
# We execute the loop (while 1 > 0) log10(n) + 1 times. This is tricky! 
# Because we divide i by 10 every time through the loop, we only execute this loop a logarithmic number of times. 
# log10(n) divisions of i by 10 will get us to i = 1; BUT we'll need one more division to get x <= 0 

print math.log(15, 2)
i = 12
print 'the result of %s is %s as a %s'%(i, intToStr(i), type(intToStr(i)))


def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    print 'smaller = ',smaller
    extra = L[-1:]
    print 'extra = ',extra
    new = []
    for small in smaller:
        new.append(small+extra)
        print 'append in loop',new
    return smaller+new

L=['a','b','c']
genSubsets(L)