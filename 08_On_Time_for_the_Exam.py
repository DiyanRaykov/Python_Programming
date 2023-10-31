hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

time_exam = hour_exam * 60 + minutes_exam
time_arrival = hour_arrival * 60 + minutes_arrival
dif = abs(time_arrival - time_exam)

hh = dif // 60
mm = dif % 60
if time_arrival > time_exam:
    print('Late')
    if hh == 0:
        print(f"{mm} minutes after the start")
    elif hh != 0:
        print(f"{hh}:{mm :02d} hours after the start")

elif time_arrival < time_exam:
    if hh == 0 and mm <= 30:
        print('On time')
        print(f"{mm} minutes before the start")
    elif hh == 0 and mm > 30:
        print('Early')
        print(f"{mm} minutes before the start")
    elif hh != 0:
        print('Early')
        print(f"{hh}:{mm :02d} hours before the start")
elif time_arrival == time_exam:
    print('On time')
