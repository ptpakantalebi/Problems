a = int(input('enter the number: '))

def isprime (n):
    i = 1
    while i < n:
        i += 1
        if n % i == 0:
            return n == i
n = 0
b = 2
while True:
    if isprime(b):
        n+=1
    if n == a:
        print(b)
        break
    b += 1