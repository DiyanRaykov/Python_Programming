import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

time_for_distance = distance_in_meters * time_in_seconds_for_one_meter
# added_seconds = distance_in_meters / 15
added_seconds = math.floor(distance_in_meters / 15) * 12.5
real_time = time_for_distance + added_seconds

slower = real_time - record_in_seconds
# faster = record_in_seconds - real_time

if record_in_seconds <= real_time:
    print(f"No, he failed! He was {slower :.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {real_time :.2f} seconds.")
