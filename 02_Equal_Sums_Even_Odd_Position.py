n1 = int(input())
n2 = int(input())

for number in range(n1, n2 + 1):
    number_str = str(number)
    x1 = number_str[0]
    x2 = number_str[2]
    x3 = number_str[4]
    y1 = number_str[1]
    y2 = number_str[3]
    y3 = number_str[5]
    odd_sum = int(x1) + int(x2) + int(x3)
    even_sum = int(y1) + int(y2) + int(y3)
    if odd_sum == even_sum:
        print(f'{number} ', end='')

#     print(odd_sum)
#     print(even_sum)
#     break
# pass
