size1 = int(input())
size2 = int(input())
all_pieces = size1 * size2
command = input()
left = all_pieces
cake_finish = False

while command != "STOP":
    take_pieces = int(command)
    left -= take_pieces
    if left <= 0:
        cake_finish = True
        break
    command = input()

if command == "STOP":
    print(f"{left} pieces are left.")
if cake_finish:
    more = abs(left)
    print(f"No more cake left! You need {more} pieces more.")
