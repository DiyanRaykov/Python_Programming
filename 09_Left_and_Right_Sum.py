import math

n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    num_left_side = int(input())
    left_sum += num_left_side

for i in range(0, n):
    num_right_side = int(input())
    right_sum += num_right_side

diff = abs(right_sum - left_sum)
# diff = math.fabs(right_sum - left_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')
