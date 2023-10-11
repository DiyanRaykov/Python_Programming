length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())
percentage = percentage / 100

volume_aquarium = length_in_cm * width_in_cm * height_in_cm
volume_liters = volume_aquarium * 0.001
occupied_space = volume_liters * percentage
liters_needed = volume_liters * (1 - percentage)

print(liters_needed)
