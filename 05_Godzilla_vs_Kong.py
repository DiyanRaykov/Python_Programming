budget = float(input())
people = int(input())
clothing_price = float(input())

decor_amount = budget * 0.10
clothing_amount = clothing_price * people

discount_clothing = 0
if people > 150:
    discount_clothing = clothing_amount * 0.10
clothing_amount -= discount_clothing            # chek the line

total_for_the_movie = decor_amount + clothing_amount
remaining_amount = budget - total_for_the_movie
needed_amount = total_for_the_movie - budget

if total_for_the_movie > budget:
    print('Not enough money!')
    print(f"Wingard needs {needed_amount :.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {remaining_amount :.2f} leva left.")
