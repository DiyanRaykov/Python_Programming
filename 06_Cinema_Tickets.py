command_1 = input()
total_tickets = 0
student_counter = 0
standard_counter = 0
kid_counter = 0

while command_1 != "Finish":
    film = command_1
    free_seats = int(input())

    command_2 = input()
    tickets_counter = 0
    while command_2 != "End":
        ticket_type = command_2
        tickets_counter += 1
        total_tickets += 1

        if ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1

        if tickets_counter == free_seats:
            break
        command_2 = input()

    student_percent = student_counter * 100 / total_tickets
    standard_percent = standard_counter * 100 / total_tickets
    kid_percent = kid_counter * 100 / total_tickets

    hall_percent = tickets_counter * 100 / free_seats
    print(f"{film} - {hall_percent:.2f}% full.")

    command_1 = input()
print(f"Total tickets: {total_tickets}")
print(f'{student_percent:.2f}% student tickets.')
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
