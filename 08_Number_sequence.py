count = int(input())
max_number = -1000000000000000000000000
min_number = 1000000000000000000000000

for i in range(1, count + 1):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
