num_of_lines = int(input())
first_nums = 0
seconds_nums = 0
for _ in range(0, num_of_lines):
    current_num = int(input())
    first_nums += current_num
for _ in range(num_of_lines, num_of_lines*2):
    current_num = int(input())
    seconds_nums += current_num

if first_nums == seconds_nums:
    print(f"Yes, sum = {first_nums}")
else:
    diff = abs(seconds_nums - first_nums)
    print(f"No, diff = {diff}")