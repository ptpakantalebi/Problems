from collections import Counter
input_text = input('enter your text please: ')
members_input_text = list(input_text)
list_alphabet = ['aA','bB','cC','dD','eE','fF','gG','hH','iI','jJ','kK','lL','mM','nN','oO','pP','qQ','rR','sS','tT','uU','vV','wW','xX','yY','zZ']
for x in range(0,len(list_alphabet)):
    count_alphabt_1 = Counter(members_input_text)
    count_alphabt_2 = Counter(members_input_text)
    count_alphabt_3 = count_alphabt_1[list_alphabet[x][0]]
    count_alphabt_4 = count_alphabt_2[list_alphabet[x][1]]
    list_alphabet[x] = f'{list_alphabet[x][0]} or {list_alphabet[x][1]} == {count_alphabt_3+count_alphabt_4}'
sort_list_alphabet = sorted(list_alphabet, key=lambda t:t[-1])
for member_list_alphabet in sort_list_alphabet:
    print(member_list_alphabet)
print()
split_input = input_text.split(' ')
for f in range(0,len(split_input)-1):
    if len(split_input[f+1]) > len(split_input[f]):
        print(split_input[f+1])
    if split_input[f][-1] == split_input[f+1][0]:
        print(split_input[f],'and',split_input[f+1])
b = Counter(split_input[0:int(len(split_input)/2)])
c = Counter(split_input[int(len(split_input)/2):])
print()
for v in c:
    for n in b:
        if v == n:
            if c[v] > b[n]:
                print(v,c[v])