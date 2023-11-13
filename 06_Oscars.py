actor_name = input()
academy_points = float(input())
number_evaluators = int(input())

text_count = 0

for _ in range(number_evaluators):
    evaluator_name = input()
    points_evaluator = float(input())
    text_count = len(evaluator_name)
    new_points = (text_count * points_evaluator) / 2
    academy_points += new_points
    if academy_points > 1250.5:
        break

needet_points = abs(1250.5 - academy_points)
if academy_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {needet_points:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
