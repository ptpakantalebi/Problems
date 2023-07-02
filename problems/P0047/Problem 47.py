from bitarray import bitarray
from datetime import datetime
import math
input_number = int(input("Enter the number that you want to get number until it: "))
date_1 = datetime.now()


#SOLVE(2)
# time_1 = datetime.now()
# bit_array = bitarray(int(input_number/2))
# bit_array.setall(1)
# print(datetime.now()-time_1)
# n = 2
# for x in range(3,int(math.sqrt(input_number))+1,2):
#     if bit_array[x-n] == 1:
#         bit_array[(x-n)*(x+1)::x] = 0
#     n += 1
# print(datetime.now()-time_1,bit_array.count(1))

#SOLVE(1)
# date_1 = datetime.now()
# bit_array = bitarray(input_number-1)
# print(datetime.now()-date_1)
# bit_array.setall(1)
# for x in range(2,int(math.sqrt(input_number))+1):
#     if bit_array[x-2] == 1:
#         bit_array[(x**2)-2::x] = 0
# print(datetime.now()-date_1,bit_array.count(1))