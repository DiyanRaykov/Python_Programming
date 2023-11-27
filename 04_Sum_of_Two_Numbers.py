start_range = int(input())
end_range = int(input())
magic_number = int(input())
combination = 0
result = 0
x1 = 0
x2 = 0

for x1 in range(start_range, end_range + 1):
    for x2 in range(start_range, end_range + 1):
        result = x1 + x2
        combination += 1
        if result == magic_number:
            break
    if result == magic_number:
        break
if result == magic_number:
    print(f"Combination N:{combination} ({x1} + {x2} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
