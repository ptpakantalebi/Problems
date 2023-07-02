import functools
input_number = (input('enter the number: '))
if input_number.isnumeric():
    print(functools.reduce(lambda a,b:a+b,range(1,input_number+1)))
else:
    print('just number is allowed!')