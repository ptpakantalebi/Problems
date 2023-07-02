a = [b for b in range(3,int(input('enter the number: '))+1,2)]
for x in a:
    w = 2
    while x * w <= a[-1]:
        if x * w in a:
            a.remove(x*w)
        w += 1
import functools
v = functools.reduce(lambda d,m:d*m,a)
print(v*2)