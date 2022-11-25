number_of_pairs = int(input())
previous_sum = int(input()) + int(input())
max_diff = 0

for _ in range(number_of_pairs - 1):
    current_sum = int(input()) + int(input())

    if abs(previous_sum - current_sum) > max_diff:
        max_diff = abs(previous_sum - current_sum)

    previous_sum = current_sum

if max_diff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_diff}")