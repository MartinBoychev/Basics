import sys

num = input()
max_num = -sys.maxsize
while True:
    if num == "Stop":
        break
    current_num = int(num)
    if current_num > max_num:
        max_num = current_num

    num = input()
print(max_num)