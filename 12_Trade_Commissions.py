city = input()
sales = float(input())

commission_amount = 0
if city == 'Sofia' and 0 <= sales <= 500:
    commission_amount = sales * 0.05
elif city == 'Sofia' and 500 < sales <= 1000:
    commission_amount = sales * 0.07
elif city == 'Sofia' and 1000 < sales <= 10000:
    commission_amount = sales * 0.08
elif city == 'Sofia' and sales > 10000:
    commission_amount = sales * 0.12

elif city == 'Varna' and 0 <= sales <= 500:
    commission_amount = sales * 0.045
elif city == 'Varna' and 500 < sales <= 1000:
    commission_amount = sales * 0.075
elif city == 'Varna' and 1000 < sales <= 10000:
    commission_amount = sales * 0.10
elif city == 'Varna' and sales > 10000:
    commission_amount = sales * 0.13

elif city == 'Plovdiv' and 0 <= sales <= 500:
    commission_amount = sales * 0.055
elif city == 'Plovdiv' and 500 < sales <= 1000:
    commission_amount = sales * 0.08
elif city == 'Plovdiv' and 1000 < sales <= 10000:
    commission_amount = sales * 0.12
elif city == 'Plovdiv' and sales > 10000:
    commission_amount = sales * 0.145

else:
    print('error')
    exit()

print(f'{commission_amount :.2f}')
