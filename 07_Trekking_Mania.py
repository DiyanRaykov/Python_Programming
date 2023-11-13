num_groups = int(input())
count_musala = 0
count_mont_blanc = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0
total_count = 0

for _ in range(num_groups):
    num_people = int(input())
    total_count += num_people
    if num_people <= 5:
        count_musala += num_people
    elif num_people <= 12:
        count_mont_blanc += num_people
    elif num_people <= 25:
        count_kilimanjaro += num_people
    elif num_people <= 40:
        count_k2 += num_people
    elif num_people > 40:
        count_everest += num_people

percent_musala = count_musala / total_count
percent_mont_blanc = count_mont_blanc / total_count
percent_kilimanjaro = count_kilimanjaro / total_count
percent_k2 = count_k2 / total_count
percent_everest = count_everest / total_count

print(f'{percent_musala:.2%}')
print(f'{percent_mont_blanc:.2%}')
print(f'{percent_kilimanjaro:.2%}')
print(f'{percent_k2:.2%}')
print(f'{percent_everest:.2%}')
