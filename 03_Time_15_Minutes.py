hour = int(input())
minutes = int(input())

hour = hour * 60
time = hour + minutes + 15

hour = time // 60
minutes = time % 60

if hour > 23:
    hour = 0
if minutes < 10:                 # по-напреднал код на тази if -else
    print(f'{hour}:0{minutes}')  # проверка е последният закоментиран ред
else:
    print(f'{hour}:{minutes}')

# print(f'{hour}:{minutes :02d}')
