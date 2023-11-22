money_needed = float(input())
cash_available = float(input())
days_count = 0
spend_count = 0
has_failed = False
while cash_available < money_needed:
    spend_or_save = input()
    money_per_day = float(input())
    days_count += 1
    if spend_or_save == "spend":
        spend_count += 1
        cash_available -= money_per_day
        if cash_available < 0:
            cash_available = 0
        if spend_count == 5:
            has_failed = True
            break
    else:   # spend_or_save == "save"
        cash_available += money_per_day
        spend_count = 0
        if cash_available >= money_needed:
            break
if has_failed:
    print("You can't save the money.")
    print(days_count)
else:
    print(f"You saved the money for {days_count} days.")
