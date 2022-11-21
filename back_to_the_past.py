heritage = float(input())
year = int(input())
age = 18
back_to = 1800
money_spent = 0
for _ in range(1800, year + 1):
    if back_to % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * age
    age += 1
    back_to += 1
diff = abs(heritage - money_spent)
if heritage >= money_spent:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")