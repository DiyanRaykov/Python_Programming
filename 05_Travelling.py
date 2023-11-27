destination = input()
while destination != 'End':
    min_budget = float(input())
    amount = 0
    while amount < min_budget:
        sum = float(input())
        amount += sum

    print(f"Going to {destination}!")
    destination = input()

