puzzles = 2.60
dolls = 3.00
bears = 4.10
minions = 8.20
trucks = 2.00

excursion_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

amount = (puzzles_number * puzzles
          + dolls_number * dolls
          + bears_number * bears
          + minions_number * minions
          + trucks_number * trucks)
toys_number = (puzzles_number
               + dolls_number
               + bears_number
               + minions_number
               + trucks_number)

discount = 0
if toys_number >= 50:
    discount = amount * 0.25
final_amount = amount - discount
rent = final_amount * 0.10
profit = final_amount - rent
remaining_amount = profit - excursion_price
needed_amount = excursion_price - profit

if profit >= excursion_price:
    print(f'Yes! {remaining_amount :.2f} lv left.')
else:
    print(f'Not enough money! {needed_amount :.2f} lv needed.')
