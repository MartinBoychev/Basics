months = int(input())
el_total = 0
water = 20 * months
internet = 15 * months

for _ in range(0, months):
    el_bill = float(input())
    el_total += el_bill

others = (el_total + water + internet) * 1.2
avg = (el_total + water + internet + others) / months

print(f"Electricity: {el_total:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {avg:.2f} lv")