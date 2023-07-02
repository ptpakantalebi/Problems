input_text = input('entert the text: ')

password = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z','27':'!','28':'?','29':'.','30':',','31':' ','32':'0','33':'1','34':'2','35':'3','36':'4','37':'5','38':'6','39':'7','40':'8','41':'9','42':':'}
list_0 = []
if input_text[0] == 'P':
    for x in list(input_text[2:]):
        for a_1 in range(1,len(password)+1):
            if x.casefold() == password[str(a_1)]:
                list_0.append(f'{a_1} ')

if input_text[0] == 'E':
    for a_2 in input_text.split(' ')[1:]:
        list_0.append(password[a_2])

print(*list_0,sep='')