input_number = int(input('enter the number: '))
for x in range(0,input_number):
    input_word_1 = input('enter the word: ')
    input_word_2 = input('enter the word: ')
    if len(input_word_1) != len(input_word_2):
        c = len(max(input_word_1,input_word_2))
        for a in min(input_word_1,input_word_2):
            if a in max(input_word_1,input_word_2):
                c -= 1
            if a not in max(input_word_1,input_word_2):
                c += 1
        print(c)
    else:
        n = 0
        for d in input_word_1:
            if d  not in input_word_2:
                n += 1
        print(n)