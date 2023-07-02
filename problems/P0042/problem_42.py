import turtle
from functools import reduce
input_pos = input('enter the positons: ').split(' ')
def pos(n):
    list_pos = []
    for a in n:
        list_pos.append((int(a.split(',')[0][1:])*30,int(a.split(',')[1][0:-1])*30))
    return list_pos
list_1 = []
for b in range(0,int(input('how many case do you want to enter: '))):
    list_1.append(pos(input('enter the position of obstacles: ').split(' ')))
circle_1 = turtle.Turtle()
circle_2 = turtle.Turtle()
circle_1.shape('circle')
circle_2.shape('circle')
circle_1.penup()
circle_1.goto(pos(input_pos)[0][0],pos(input_pos)[0][1])
circle_1.pendown()
circle_2.penup()
circle_2.goto(pos(input_pos)[1][0],pos(input_pos)[1][1])
circle_2.pendown()
laki = turtle.Turtle()
laki.speed(1)
for c in list_1:
    laki.penup()
    laki.goto(c[0][0],c[0][1])
    laki.pendown()
    for d in range(1,len(c)):
        laki.goto(c[d][0],c[d][1])
laki.color('blue')
laki.penup()
laki.goto(pos(input_pos)[0][0],pos(input_pos)[0][1])
laki.pendown()
go = pos(input_pos)[0]
last_position = reduce(lambda x,y:x+y,list_1)
while go != pos(input_pos)[1]:
    side = (go[0]-pos(input_pos)[1][0],go[1]-pos(input_pos)[1][1])
    if 
            
#case 1
# (4,2) (7,9)
# 6
# (2,1) (2,2) (3,2) (3,3) (4,3) (5,3) (5,2) (6,2) (7,2)
# (7,4) (7,3) (8,3)
# (10,2) (10,3) (10,4) (10,5) (10,6) (9,6) (8,6) (7,6)
# (7,7) (6,7) (6,6) (5,6)
# (3,5) (3,6) (4,6)
# (4,8) (3,8) (3,9) (4,9) (5,9) (5,10)
#case 2
# (4,2) (7,9)
# 4
# (8,3) (7,3)
# (7,5) (7,4) (6,4)
# (7,6) (8,6) (9,6) (10,6) (10,5) (10,4) (10,3) (10,2)
# (6,1) (6,2) (6,3) (5,3) (5,4) (5,5) (4,5) (3,5) (3,4) (3,3) (3,2) (2,2) (2,1) (3,1) (4,1) (5,1) (6,1)
input()