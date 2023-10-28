projection_type = input()
rows = int(input())
columns = int(input())

price = 0
if projection_type == 'Premiere':
    price = 12.00
elif projection_type == 'Normal':
    price = 7.50
elif projection_type == 'Discount':
    price = 5.00

total_ticket_amount = rows * columns * price
print(f'{total_ticket_amount :.2f} leva')
