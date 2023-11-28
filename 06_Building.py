last_floor = int(input())
rooms = int(input())
index = ''

for current_floor in range(last_floor, 0, -1):
    if current_floor == last_floor:
        index = 'L'
    elif current_floor % 2 == 0:
        index = 'O'
    else:
        index = 'A'
    t = ''
    for current_rooms in range(rooms):
        t = t + index + str(current_floor) + str(current_rooms) + ' '
        #print(f'{index}{current_floor}{current_rooms}', end=' ')
    print(t)
    #print()
