# hour = int(input())
# day = input()
#
# if 10 <= hour <= 18 and\
#     (day == 'Monday'
#      or day == 'Tuesday'
#      or day == 'Wednesday'
#      or day == 'Thursday'
#      or day == 'Friday'
#      or day == 'Saturday'):
#     print('open')
# else:
#     print('closed')

# Горното решение е правилно, но
# долното е с по-добра логика и по-кратко

hour = int(input())
day = input()

if day == 'Sunday' or not 10 <= hour <= 18:
    print('closed')
else:
    print('open')
