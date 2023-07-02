input_text_1 = int(input('enter the number: '))
list_1 = []
for a in range(0,input_text_1):
    list_1.append(input('enter: ').split(' '))
while True:
    list_2 = []
    input_city = input('enter the city: ')
    if input_city == 'END':
        break
    for b in input_city:
        for c in list_1:
            if c[0] == b:
                list_2.append(c)
    total = 0
    for d in range(0,len(list_2)-1):
        x_1,y_1 = (int(list_2[d][1]),int(list_2[d][2]))
        x_2,y_2 = (int(list_2[d+1][1]),int(list_2[d+1][2]))
        if x_1-x_2 <= 0:
            total += (x_1-x_2)*-1
        else:
            total += x_1-x_2
        if y_1-y_2 < 0:
            total += (y_1-y_2)*-1
        else:
            total += y_1-y_2
    print(total)
# A 2 0
# B 2 4
# C 5 2
# D 7 0
# E 0 7