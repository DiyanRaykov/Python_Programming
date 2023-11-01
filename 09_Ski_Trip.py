bgn_person = 18.00
bgn_apartment = 25.00
bgn_president = 35.00

days_of_stay = int(input())
room_type = input()
evaluation = input()
nights_of_stay = days_of_stay - 1

amount = 0
if room_type == "room for one person":
    amount = bgn_person * nights_of_stay

if room_type == "apartment" and days_of_stay < 10:
    amount = bgn_apartment * nights_of_stay * (1 - 0.30)
elif room_type == "apartment" and 10 <= days_of_stay <= 15:
    amount = bgn_apartment * nights_of_stay * (1 - 0.35)
elif room_type == "apartment" and days_of_stay > 15:
    amount = bgn_apartment * nights_of_stay * (1 - 0.50)

if room_type == "president apartment" and days_of_stay < 10:
    amount = bgn_president * nights_of_stay * (1 - 0.10)
elif room_type == "president apartment" and 10 <= days_of_stay <= 15:
    amount = bgn_president * nights_of_stay * (1 - 0.15)
elif room_type == "president apartment" and days_of_stay > 15:
    amount = bgn_president * nights_of_stay * (1 - 0.20)

if evaluation == "positive":
    amount *= (1 + 0.25)
else:
    amount *= (1 - 0.10)

print(f'{amount :.2f}')
