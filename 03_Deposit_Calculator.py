amount_deposited = float(input())
term_of_the_deposit_in_months = float(input())
annual_interest_rate = float(input())

annual_interest_rate = annual_interest_rate / 100
amount = amount_deposited + term_of_the_deposit_in_months * ((amount_deposited * annual_interest_rate) / 12)

print(amount)

