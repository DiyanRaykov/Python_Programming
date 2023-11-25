size1 = int(input())
size2 = int(input())
size3 = int(input())
all_cubic_meters = size1 * size2 * size3
left_cubic_meters = all_cubic_meters
command = input()
has_not_space = False

while command != "Done":
    luggage = int(command)
    left_cubic_meters -= luggage
    if left_cubic_meters <= 0:
        has_not_space = True
        break
    command = input()

if command == "Done":
    print(f"{left_cubic_meters} Cubic meters left.")
if has_not_space:
    needed = - left_cubic_meters
    print(f"No more free space! You need {needed} Cubic meters more.")
