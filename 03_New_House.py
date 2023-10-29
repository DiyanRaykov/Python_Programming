flower_type = input()
number_of_flowers = int(input())
budget = int(input())

price = 0
if flower_type == 'Roses':
    if number_of_flowers > 80:
        price = number_of_flowers * 5 * (1 - 0.1)
    else:
        price = number_of_flowers * 5
if flower_type == 'Dahlias':
    if number_of_flowers > 90:
        price = number_of_flowers * 3.80 * (1 - 0.15)
    else:
        price = number_of_flowers * 3.80
if flower_type == 'Tulips':
    if number_of_flowers > 80:
        price = number_of_flowers * 2.80 * (1 - 0.15)
    else:
        price = number_of_flowers * 2.80
if flower_type == 'Narcissus':
    if number_of_flowers < 120:
        price = number_of_flowers * 3 * (1 + 0.15)
    else:
        price = number_of_flowers * 3
if flower_type == 'Gladiolus':
    if number_of_flowers < 80:
        price = number_of_flowers * 2.5 * (1 + 0.2)
    else:
        price = number_of_flowers * 2.5

amount = abs(budget - price)
if budget < price:
    print(f"Not enough money, you need {f'{amount :.2f}'} leva more.")
else:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {f'{amount :.2f}'} leva left.")
