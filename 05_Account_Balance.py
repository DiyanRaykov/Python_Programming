total = 0
command = input()
while command != 'NoMoreMoney':
    increase = float(command)
    if increase < 0:
        print(f"Invalid operation!")
        break
    print(f'Increase: {increase:.2f}')
    total += increase
    command = input()
print(f"Total: {total:.2f}")
