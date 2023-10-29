budget = int(input())
season = input()
number_fishermen = int(input())

renting_the_ship = 0
# discount = 0
if season == "Spring":
    renting_the_ship = 3000
elif season == "Summer" or season == "Autumn":
    renting_the_ship = 4200
elif season == "Winter":
    renting_the_ship = 2600

if number_fishermen <= 6:
    renting_the_ship *= (1 - 0.10)
elif 7 <= number_fishermen <= 11:
    renting_the_ship *= (1 - 0.15)
else:
    renting_the_ship *= (1 - 0.25)

if number_fishermen % 2 == 0 and season != "Autumn":
    renting_the_ship *= (1 - 0.05)

amount = abs(budget - renting_the_ship)
if budget < renting_the_ship:
    print(f"Not enough money! You need {amount :.2f} leva.")
else:
    print(f"Yes! You have {amount :.2f} leva left.")
