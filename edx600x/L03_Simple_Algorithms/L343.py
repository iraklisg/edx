# lecture 3.4, slide 3

num = 302 # = 100101110

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0: #
    print num
    result = str(num%2)+result # to vazei prin to result, alliws, result =result + num%2 (or result += num%2) mas dinei inverted apotelesma
    print 'result is ',result
    num = num/2 #shift right
    print 'new num/2 is ',num
    print '========================'
if isNeg:
    result = '-' + result