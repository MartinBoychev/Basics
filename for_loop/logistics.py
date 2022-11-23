count_cargo = int(input())

bus = 0
truck = 0
train = 0
total_weight = 0

for _ in range(1, count_cargo + 1):
    cargo = int(input())
    if cargo <= 3:
        bus += cargo
        total_weight += cargo
    elif cargo <= 11:
        truck += cargo
        total_weight += cargo
    elif cargo > 11:
        train += cargo
        total_weight += cargo

total_price = bus * 200 + truck * 175 + train * 120
avg_price = total_price / total_weight
print(f"{avg_price:.2f}")
print(f"{bus / total_weight * 100:.2f}%")
print(f"{truck / total_weight * 100:.2f}%")
print(f"{train / total_weight * 100:.2f}%")