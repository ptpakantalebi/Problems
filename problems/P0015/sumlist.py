list_0 = []
while True:
    input_number = input('enter the number: ')
    if input_number == 'END':
        break
    list_0.append(int(input_number))
def sumlist(n):
    total = 0
    for x in n:
        total += x
    return total
print(sumlist(list_0))