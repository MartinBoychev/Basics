import sys

num = input()
min_num = sys.maxsize
while True:
    if num == "Stop":
        break
    current_num = int(num)
    if current_num < min_num:
        min_num = current_num

    num = input()
print(min_num)