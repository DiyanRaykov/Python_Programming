budget = float(input())
number_of_video_cards = int(input())
number_of_processors  = int(input())
number_of_ram = int(input())

video_card_per_one = 250
video_amount = video_card_per_one * number_of_video_cards
processor_bg = 0.35 * video_amount
processor_amount = processor_bg * number_of_processors
ram_bg = 0.10 * video_amount
ram_amount = ram_bg * number_of_ram

total_amount = video_amount + processor_amount + ram_amount

if number_of_processors < number_of_video_cards:
    total_amount = total_amount * 0.85

needed = total_amount - budget
enough = budget - total_amount

if budget >= total_amount:
    print(f"You have {enough :.2f} leva left!")
else:
    print(f"Not enough money! You need {needed :.2f} leva more!")
