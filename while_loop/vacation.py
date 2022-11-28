excursion_price = float(input())
amount_money = float(input())

total_days = 0
spending_days = 0
saving_days = 0
total_sum = amount_money

while total_sum < excursion_price and spending_days < 5:
    action = input()
    amount_action = float(input())
    total_days += 1
    if action == "spend":
        spending_days += 1
        if amount_action >= total_sum:
            total_sum = 0
        else:
            total_sum -= amount_action

    elif action == "save":
        saving_days += 1
        total_sum += amount_action
        spending_days = 0

if total_sum >= excursion_price:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)