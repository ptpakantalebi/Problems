from collections import namedtuple
from functools import reduce
a = int(input('enter the number: '))
pos = namedtuple('pos',['x','y'])
def is_adjacent(a,b):
    return abs(a.x - b.x) <= 1 and abs(a.y - b.y) <= 1
list_1 = []
for b in range(0,a):
    list_1.append(input('enter the karekter: ').split(' '))
while True:
    word_input = input('enter the word: ')
    if word_input == 'END':
        break
    list_3 = []
    s = True
    for d in word_input:
        list_2 = []
        o = len(list_1)
        for e in range(0,a):
            if d not in list_1[e]:
                o -= 1
            for f in range(0,a):
                if d == list_1[e][f]:
                    list_2.append(pos(e,f))
        if o == 0:
            s = False
            break
        list_3.append(list_2)
    if s:
        result = list_3[0]
        def merge(x, y):
            if isinstance(y, list) and not isinstance(x, list) :
                z = y.copy()
                z.append(x)
                return z
            elif not isinstance(x, list) and not isinstance(y, list):
                return [x,y]
            elif isinstance(x, list) and isinstance(y, list):
                return x + y
            elif isinstance(x, list) and not isinstance(y, list):
                z = x.copy()
                z.append(y)
                return z
        def concat(x, y):
            result = []
            for item in x:
                result.append(item)
            for item in y:
                result.append(item)
            return result
        for index in range(1, len(list_3)):
            next = list_3[index]
            result = list(map(lambda x: list(map(lambda y: merge(y, x),  result)), next))
            result = reduce(lambda x, y: x + y, result)
            
        for x in result:
            l = len(x)
            for t in range(0,len(x)-1):
                if is_adjacent(x[t],x[t+1]):
                    l -= 1
            if l == 1:
                print(x)
    else:
        print(f'{word_input} is not found')
# w r s t y
# u o h o f
# i d s n a
# m b v c x
# l k j p q