# import sys
#
# command = input()
# max_number = -sys.maxsize
#
# while command != "Stop":
#     number = int(command)
#     if max_number < number:
#         max_number = number
#     else:
#         command = input()
# print(max_number)

#долното решение е същото, но без else,
# а с отместване на command = input()

import sys

command = input()
max_number = -sys.maxsize

while command != "Stop":
    number = int(command)
    if max_number < number:
        max_number = number
    command = input()
print(max_number)
