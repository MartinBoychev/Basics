price_20kg = float(input())
kg_bag = float(input())
days = int(input())
count_bags = int(input())
price = 0

if 0 < kg_bag < 10:
    price = price_20kg * 0.2
elif 10 <= kg_bag <= 20:
    price = price_20kg * 0.5
elif kg_bag > 20:
    price = price_20kg

if days > 30:
    price *= 1.10
elif 30 >= days >= 7:
    price *= 1.15
elif days < 7:
    price *= 1.40

print(f"The total price of bags is: {price * count_bags:.2f} lv. ")