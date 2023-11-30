number = int(input())

for n in range(1111, 10000):
    n_as_str = str(n)
    is_special = True


    for idx, digit in enumerate(n_as_str):
        digit_as_int = int(digit)

        if digit_as_int == 0:
            is_special = False
            break

        if number % digit_as_int != 0:
            is_special = False
            break
    if is_special:
        print(f'{n} ', end='')
