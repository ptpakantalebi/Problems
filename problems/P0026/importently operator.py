input_number = input().split(' ')

def eval(n):
    if '*' in n or '/' in n:
        for x in range(0,len(n)):
            if n[x] == '*':
                total_1 = float(n[x-1])*float(n[x+1])
                break
            if n[x] == '/':
                total_1 = float(n[x-1])/float(n[x+1])
                break
        del n[x-1:x+2]
        n.insert(x-1,total_1)
    else:
        if n[1]=='+':
            total_2 = float(n[0])+float(n[2])
        if n[1]=='-':
            total_2 = float(n[0])-float(n[2])
        del n[0:3]
        n.insert(0,total_2)

if '(' in input_number:
    list_1 = []
    list_2 = []
    for a in input_number:
        if a == ')':
            while list_1[-1] != '(':
                list_2.append(list_1.pop())
            list_1.pop(-1)
            list_2.reverse()
            while len(list_2) != 1:
                eval(list_2)
            list_1.append(list_2[0])
            list_2.clear()
        else:
            list_1.append(a)
    if len(list_1) > 1:
        while len(list_1) != 1:
            eval(list_1)
    print(list_1[0])

else:
    while len(input_number) != 1:
        eval(input_number)
    print(input_number[0])