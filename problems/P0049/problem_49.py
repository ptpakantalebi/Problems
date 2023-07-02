import math
from collections import namedtuple
from textwrap import indent
a = input().split(' ')
list_0 = []
planet = namedtuple('planet',['h','w'])
for b in range(0,int(input('enter the number: '))):
    c = input().split(' ')
    list_0.append(planet(c[1],c[2]))
    list_0.append(c[0])
pos_1,pos_2 = input().split(' ')
first_planet = input('enter the name of planet: ')
distance_0 = math.sqrt(((int(pos_1)-int(list_0[list_0.index(first_planet)-1][0]))**2)+((int(pos_2)-int(list_0[list_0.index(first_planet)-1][1]))**2))
print(f'{(distance_0*8.3)*60:<10.2f} {first_planet}')
while len(list_0) != 2:
    list_1 = []
    for d in range(0,len(list_0),2):
        if list_0.index(first_planet) != d+1:
            list_1.append((((int(list_0[d][0])-int(list_0[list_0.index(first_planet)-1][0]))**2)+((int(list_0[d][1])-int(list_0[list_0.index(first_planet)-1][1]))**2),list_0[d+1]))
    distance_1 = math.sqrt(((int(pos_1)-int(list_0[list_0.index(min(list_1)[1])-1][0]))**2)+((int(pos_2)-int(list_0[list_0.index(min(list_1)[1])-1][1]))**2))
    print(f'{(distance_1*8.3)*60:<10.2f} {min(list_1)[1]}')
    list_0.remove(list_0[list_0.index(first_planet)-1])
    list_0.remove(list_0[list_0.index(first_planet)])
    first_planet = min(list_1)[1]
    # list_0.