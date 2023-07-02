c = int(input('enter the numebr: '))

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)
y = 1
while True:
    a = fibonacci (y)
    if a > c:
        break
    print(a)
    y += 1