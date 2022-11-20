n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
count_nums = 0

for i in range(0, n):
    num = int(input())
    count_nums += 1
    if 0 < num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1

print(f"{p1 / count_nums * 100:.2f}%")
print(f"{p2 / count_nums * 100:.2f}%")
print(f"{p3 / count_nums * 100:.2f}%")
print(f"{p4 / count_nums * 100:.2f}%")
print(f"{p5 / count_nums * 100:.2f}%")