import functools
print(functools.reduce(lambda a,b:a*b,range(1,int(input('enter the number: '))+1)))