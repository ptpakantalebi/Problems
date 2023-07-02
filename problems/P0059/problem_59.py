input_number = int(input('enter the number: '))
list_numbers = ['0','1','2','3','4','5','6','7','8','9']
list_character_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_character_2 = [':',';',',','.',"'",'@','?','!','#','&','*','-','/','%','^']
for a in range(0,input_number):
    input_character = input('enter the Specifications: ').split(' ')
    for b in range(0,int(input('how many case do you want to enter: '))):
        input_password = input('enter the word: ')
        if len(input_password) >= int(input_character[2][2]):
            len_1,len_2,len_3 = (0,0,0)
            for c in input_password:
                if c.casefold() in list_numbers:
                    len_1 += 1
                if c.casefold() in list_character_1:
                    len_2 += 1
                if c.casefold() in list_character_2:
                    len_3 += 1
            if len_1 < int(input_character[0][2]):
                print(f"'{input_password}' must have at least {input_character[0][2]} numerics.")
            if len_2 < int(input_character[1][2]):
                print(f"'{input_password} 'must have at least {input_character[1][2]}")
            if len_3 < int(input_character[3][2]):
                print(f"'{input_password}' must have at least {input_character[3][2]} punctuation marks.")
            if len_1 >= int(input_character[0][2]) and len_2 >= int(input_character[1][2]) and len_3 >= int(input_character[3][2]):
                print(f"'{input_password}'is valid")
        else:
            print(f"'{input_password}'length is less than {input_character[2][2]} characters")