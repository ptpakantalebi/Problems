input_text = input('enter the text: ').split(' ')

if input_text[0][0] == 'P':
    input_text.pop(0)
    list_1 = []
    dict_0 = {}
    b = 0
    for a in set(input_text):
        dict_0[a] = b
        b += 1
    for b in input_text:
        for c in dict_0:
            if b == c:
                print(dict_0[c])
                break

if input_text[0][0] == 'E':
    input_text.pop(0)
    list_2 = []
    while True:
        words = input('enter the word: ')
        if words == 'END':
            break
        list_2.append(words)
    print(list_2)