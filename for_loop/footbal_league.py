capacity_stadium = int(input())
num_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
per_a = 0
per_b = 0
per_v = 0
per_g = 0
per_all = 0

for _ in range(0, num_fans):
    if num_fans > capacity_stadium:
        break
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

per_a = sector_a * 100 / num_fans
per_b = sector_b * 100 / num_fans
per_v = sector_v * 100 / num_fans
per_g = sector_g * 100 / num_fans
per_all = (num_fans / capacity_stadium) * 100

print(f"{per_a:.2f}%")
print(f"{per_b:.2f}%")
print(f"{per_v:.2f}%")
print(f"{per_g:.2f}%")
print(f"{per_all:.2f}%")
