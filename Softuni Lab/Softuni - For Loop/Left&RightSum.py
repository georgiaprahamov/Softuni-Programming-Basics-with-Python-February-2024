n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    left_sum += int(input())

for _ in range(n):
    right_sum += int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")