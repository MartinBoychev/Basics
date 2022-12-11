money_per_day = float(input())
profit_per_day = float(input())
spending = float(input())
price_gift = float(input())

total = money_per_day * 5 + profit_per_day * 5 - spending
diff = abs(total - price_gift)

if total >= price_gift:
    print(f"Profit: {total:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")