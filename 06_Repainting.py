nylon_bgn = 1.50
paint_bgn = 14.50
thinner_bgn = 5.00

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

amount_of_nylon = (nylon + 2) * nylon_bgn
amount_of_paint = (paint + paint * 0.1) * paint_bgn
amount_of_thinner = thinner * thinner_bgn
amount_of_bags = 0.40

all_materials = amount_of_nylon + amount_of_paint + amount_of_thinner + amount_of_bags
amount_of_work = (all_materials * 0.3) * hours
all_amount = all_materials + amount_of_work

print(all_amount)
