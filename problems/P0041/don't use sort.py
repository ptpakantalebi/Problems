a = input('enter the numbers: ')
b = a.split(' ')
c = list(map(lambda d:int(d),b))
while len(c):
    for d in c:
        f = 0
        for e in c:
            if d < e or d == e:
                f += 1
                if f == len(c):
                    print(d)
                    c.remove(d)