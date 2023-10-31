month = input()
overnight = int(input())

studio = 0
apartment = 0
if month == 'May' or month == 'October':
    studio = 50 * overnight
    apartment = 65 * overnight
    if 7 < overnight <= 14:
        studio *= (1 - 0.05)
    elif overnight > 14:
        studio *= (1 - 0.30)
elif month == 'June' or month == 'September':
    studio = 75.20 * overnight
    apartment = 68.70 * overnight
    if overnight > 14:
        studio *= (1 - 0.20)
elif month == 'July' or month == 'August':
    studio = 76 * overnight
    apartment = 77 * overnight

if overnight > 14:
    apartment *= (1 - 0.10)

print(f"Apartment: {apartment :.2f} lv.")
print(f"Studio: {studio :.2f} lv.")
