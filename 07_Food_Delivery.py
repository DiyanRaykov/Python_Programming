chicken_menu = 10.35
fish_menu = 12.40
veg_menu = 8.15

num_chicken_menu = int(input())
num_fish_menu = int(input())
num_veg_menu = int(input())

chicken_amount = chicken_menu * num_chicken_menu
fish_amount = fish_menu * num_fish_menu
veg_amount = veg_menu * num_veg_menu
menues_amount = chicken_amount + fish_amount + veg_amount
desert = menues_amount * 0.2
delivery = 2.5
all_amount = menues_amount + desert + delivery

print(all_amount)