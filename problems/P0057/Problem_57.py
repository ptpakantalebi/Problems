import xlrd
list_0 = []
sheet = xlrd.open_workbook(input('enter the excel file: '))

sheet_student_1 = sheet.sheet_by_index(0)
sheet_student_2 = sheet.sheet_by_index(1)
sheet_student_3 = sheet.sheet_by_index(2)

input_id = int(input('enter the id of a preson: '))
print('student info:')
for x in range(sheet_student_1.nrows):
    if sheet_student_1.cell_value(x,0) == input_id:
        print('id: ',int(sheet_student_1.cell_value(x,0)))
        print('Name: ',sheet_student_1.cell_value(x,1))
        break

print(sheet_student_1.cell_value(x,1),'Courses: ')
for i in range(sheet_student_3.nrows):
    if sheet_student_3.cell_value(i,0) == input_id:
        list_0.append(sheet_student_3.cell_value(i,1))
for b in list_0:
    print(f'{int(b)}: {sheet_student_2.cell_value(int(b)-1,1)}')