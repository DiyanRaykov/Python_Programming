bad_score = int(input())
task_name = input()
current_score = int(input())
total_score = 0
average_score = 0
counter = 0
bad_counter = 0
while task_name != "Enough":
    counter += 1
    total_score += current_score
    average_score = total_score / counter
    if current_score <= 4:
        bad_counter += 1
        if bad_counter == bad_score:
            print(f"You need a break, {bad_counter} poor grades.")
            break
    old_task = task_name
    task_name = input()
    if task_name == "Enough":
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {counter}")
        print(f"Last problem: {old_task}")
        break
    current_score = int(input())
