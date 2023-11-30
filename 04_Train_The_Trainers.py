trainers_number = int(input())
command = input()
total_grade = 0
counter = 0

while command != "Finish":
    counter += 1
    presentation = command
    presentation_average = 0
    all_ratings = 0

    for _ in range(trainers_number):
        rating = float(input())
        all_ratings += rating

    presentation_average = all_ratings / trainers_number
    total_grade += presentation_average
    print(f"{presentation} - {presentation_average:.2f}.")

    command = input()
final_grade = total_grade / counter
print(f"Student's final assessment is {final_grade:.2f}.")
