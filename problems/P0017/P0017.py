input_number = int(input('enter the number: '))
for x in range(input_number,-1,-1):
    print(x*'+'+(input_number-x)*'0')