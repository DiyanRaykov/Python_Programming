import math

num_tournaments = int(input())
start_points = int(input())
new_points = 0
num_win = 0

for _ in range(num_tournaments):
    progress = input()  # "W", "F" or "SF"
    if progress == "W":
        new_points += 2000
        num_win += 1
    elif progress == "F":
        new_points += 1200
    elif progress == "SF":
        new_points += 720

average_points = math.floor((new_points / num_tournaments))
percent_win = num_win / num_tournaments
total_points = start_points + new_points

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_win:.2%}")
