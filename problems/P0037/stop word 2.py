input_text = input('enter the text: ')
list_input_text = list(input_text)
while True:
    input_word = input('enter the word: ')
    if input_word == 'END':
        break
    start = 0
    end = 0
    for x in range(0,len(list_input_text)):
        if list_input_text[x] == ' ':
            end += (x-1)-end
            if input_word == ''.join(list_input_text[start:end+1]):
                del input_word[start:end+1]
            start += (x+1)-start
        if input_text[x] == '?' or input_text[x] == ',' or input_text[x] == '.' or input_text[x] == '!':
            if input_word == ''.join(input_word[start:end+1]):
                del input_word[start:end+1]
            start += (x+2)-start
print(input_text)