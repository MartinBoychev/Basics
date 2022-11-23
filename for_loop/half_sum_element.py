import sys

n = int(input())
sum_numbers = 0
max_num = -sys.maxsize

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {sum_numbers - max_num}")
else:
    diff = abs((sum_numbers - max_num) - max_num)
    print("No")
    print(f"Diff = {diff}")