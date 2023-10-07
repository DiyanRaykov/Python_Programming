square_meters = float(input())

price_for_meter = 7.61
price_for_landscaping = square_meters * price_for_meter
the_discount = price_for_landscaping * 0.18
amount = price_for_landscaping - the_discount

print(f'The final price is: {amount} lv.')
print(f'The discount is: {the_discount} lv.')
