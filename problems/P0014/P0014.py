input_number_1 = int(input('enter the number: '))
input_number_2 = int(input('enter the number: '))
list_1 = []
list_2 = []
for x_1 in range(input_number_1):
    list_1.append(input('enter the namde: '))
for x_2 in range(input_number_2):
    list_2.append(input('enter the name: '))
def merge(n,m):
    return n+m

print(merge(list_1,list_2))