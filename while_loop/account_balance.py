money = input()
total_sum = 0

while money != "NoMoreMoney":
    loop_money = float(money)

    if loop_money < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {loop_money:.2f}")
        total_sum += loop_money
        money = input()

print(f"Total: {total_sum:.2f}")