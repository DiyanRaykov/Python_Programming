firstCompetitor = int(input())
secondCompetitor = int(input())
thirdCompetitor = int(input())

time = firstCompetitor + secondCompetitor + thirdCompetitor

minutes = time // 60
seconds = time % 60

# Това решение е даденото в упражненията и работи вярно:
# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')

# Следващото решение също е вярно и е допълнително дадено
# форматиране от преподавателя:

print(f'{minutes}:{seconds :02d}')

