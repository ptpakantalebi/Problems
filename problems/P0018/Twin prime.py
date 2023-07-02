def isprime (a):
    i = 1
    while i < a:
        i += 2
        if a % i == 0:
            return a == i
for t in range(2,int(input('enter the number: '))+1):
    if(isprime(t)):
        if(isprime(t+2)):
            print(t,t+2)