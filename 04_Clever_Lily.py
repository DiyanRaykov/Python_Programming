lily_age = int(input())
price_wash = float(input())
price_toy = int(input())
odd = 0
even = 0
toys_amount = 0
money_amount = 0

for age in range(1, lily_age + 1, 2):
    odd += 1
    toys_amount = odd * price_toy
for age in range(2, lily_age + 1, 2):
    even += 1
    money_amount += even * 10 - 1

amount = toys_amount + money_amount
diff = abs(price_wash - amount)

if amount >= price_wash:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
