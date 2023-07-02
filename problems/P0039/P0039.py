input_number = int(input('enter the number: '))
list_0 = []
list_1 = []
input_list_1 = input('enter the numbers: ').split(' ')

for a in range(0,input_number-1):
    input_list_2 = input('enter the numbers: ').split(' ')
    list_0.append(input_list_2)

for b in input_list_1:
    t = 1
    for c in list_0:
        if b in c:
            t += 1
    if t == input_number:
        list_1.append(b)
print(set(list_1))