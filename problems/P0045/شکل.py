import turtle

laki = turtle.Turtle()
input1 = input()
input2 = input()

if input1 == 'Rectangle':
    n = input2.split(' ')
    for a in range(1,5):
        if a % 2 != 0:
            laki.forward(int(n[0]))
        else:
            laki.forward(int(n[1]))
        laki.right(90)

if input1 == 'Square':

    for x in range(0,4):
        laki.forward(int(input2))
        laki.right(90)

if input1 == 'triangle':
    for b in range(0,3):
        laki.forward(int(input2))
        laki.left(120)

if input1 == 'Circle':
    for x in range(0,36):
        laki.forward(int(input2))
        laki.left(10)

if input1 == 'pentagon':
    laki.forward(int(input2))
    for w in range(0,4):
        laki.left(72)
        laki.forward(int(input2))

if input1 == 'Oval':
    for x in range(2):     
        laki.circle(int(input2),90)
        laki.circle(int(input2)//2,90)
    laki.seth(-45)