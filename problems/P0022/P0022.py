input_number_1 = input('enter the number: ').split(' ')
input_number_2 = input('enter the number: ').split(' ')
list = []
for x in range(0,len(input_number_1)):
    list.append(int(input_number_1[x])+int(input_number_2[x]))
print(*list,sep=' ')