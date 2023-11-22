goal = 10000
command = input()
progres = 0
is_reached = False

while command != "Going home":
    current_steps = int(command)
    progres += current_steps
    if progres >= goal:
        is_reached = True
        break
    command = input()

diff = abs(progres - goal)
if is_reached:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")

if command == "Going home":
    current_steps = int(input())
    progres += current_steps
    diff = abs(progres - goal)
    if progres >= goal:
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
    else:
        print(f"{diff} more steps to reach goal.")
