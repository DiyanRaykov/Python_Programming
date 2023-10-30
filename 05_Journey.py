budget = float(input())
seasons = input()

cost = 0
destination = ''
place = ''
if budget <= 100:
    destination = 'Bulgaria'
    if seasons == "summer":
        cost = budget * 0.30
        place = 'Camp'
    elif seasons == "winter":
        cost = budget * 0.70
        place = 'Hotel'

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if seasons == "summer":
        cost = budget * 0.40
        place = 'Camp'
    elif seasons == "winter":
        cost = budget * 0.80
        place = 'Hotel'

elif budget > 1000:
    destination = 'Europe'
    cost = budget * 0.90
    place = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{place} - {cost :.2f}")
