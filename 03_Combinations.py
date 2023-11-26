sum = int(input())
count = 0
for x1 in range(sum + 1):
    for x2 in range(sum + 1):
        for x3 in range(sum + 1):
            result = x1 +x2 +x3
            if result == sum:
                count += 1
print(count)

