fruit = input()
day = input()
quantity = float(input())

if (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
    and fruit == 'banana':
    price = 2.50
elif (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
    and fruit == 'apple':
    price = 1.20
elif (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
    and fruit == 'orange':
    price = 0.85
elif (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
    and fruit == 'grapefruit':
    price = 1.45
elif (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
    and fruit == 'kiwi':
    price = 2.70
elif (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
    and fruit == 'pineapple':
    price = 5.50
elif (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday')\
    and fruit == 'grapes':
    price = 3.85

elif (day == 'Saturday' or day == 'Sunday') and fruit == 'banana':
    price = 2.70
elif (day == 'Saturday' or day == 'Sunday') and fruit == 'apple':
    price = 1.25
elif (day == 'Saturday' or day == 'Sunday') and fruit == 'orange':
    price = 0.90
elif (day == 'Saturday' or day == 'Sunday') and fruit == 'grapefruit':
    price = 1.60
elif (day == 'Saturday' or day == 'Sunday') and fruit == 'kiwi':
    price = 3.00
elif (day == 'Saturday' or day == 'Sunday') and fruit == 'pineapple':
    price = 5.60
elif (day == 'Saturday' or day == 'Sunday') and fruit == 'grapes':
    price = 4.20

else:
    print('error')
    exit()
amount = quantity * price
print(f'{amount :.2f}')
