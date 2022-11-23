age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
toys = 0
money = 0
theft = 0
total_sum = 0
for i in range (1, age + 1):
    if i % 2 == 0:
        money += 10
        theft += 1
        total_sum = total_sum + money
    else:
        toys += 1

total_money = (total_sum - theft) + toys * toy_price
diff = abs(total_money - price_washing_machine)

if total_money >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
