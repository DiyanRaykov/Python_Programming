points = int(input())
bonusScore = 0.0

if points <= 100:
    bonusScore = 5
elif 100 < points <= 1000:
    bonusScore = points * 0.2
else:
    bonusScore = points * 0.1

if points % 2 == 0:
    bonusScore = bonusScore + 1

if points % 10 == 5:
    bonusScore = bonusScore + 2

print(bonusScore)
print(points + bonusScore)