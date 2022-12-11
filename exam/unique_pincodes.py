first_num = int(input())
sec_num = int(input())
third_num = int(input())

for i in range(1, first_num + 1):
    for u in range(1, sec_num + 1):
        for y in range(1, third_num + 1):
            if i % 2 == 0 and y % 2 == 0 and 2 <= u <= 7 and u != 4 and u != 6:
                print(f"{i} {u} {y}")
