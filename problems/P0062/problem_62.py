import xlrd
input_excel = input('enter the excel file: ')
sheet = xlrd.open_workbook(input_excel)
sh = sheet.sheet_by_index(0)
for x in range(sh.nrows):
    print(f'{sh.cell_value(x,0)} is {sh.cell_value(x,1)}')