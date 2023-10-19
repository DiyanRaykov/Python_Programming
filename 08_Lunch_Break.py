import math

name_series = input()
episode_duration = int(input())
rest_duration = int(input())

lunch_time = rest_duration / 8
rest_time = rest_duration / 4
time_left = rest_duration - lunch_time - rest_time
remaining_time = time_left - episode_duration
needed_time = episode_duration - time_left

if time_left >= episode_duration:
    print(f"You have enough time to watch {name_series} "
          f"and left with {math.ceil(remaining_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, "
          f"you need {math.ceil(needed_time)} more minutes.")
