days = int(input())
money_per_day = 0
money_sum = 0
wins = 0
wins_per_day = 0
loses = 0
loses_per_day = 0
day_finished = 0
sport = input()

while True:
    if sport == "Finish":
        day_finished += 1
        if wins_per_day > loses_per_day:
            money_per_day *= 1.1
            money_sum += money_per_day
            money_per_day = 0
            wins_per_day = 0
            loses_per_day = 0
        else:
            money_sum += money_per_day
            money_per_day = 0
            wins_per_day = 0
            loses_per_day = 0
        if day_finished == days:
            break
    if sport != "Finish":
        result = input()
        if result == "win":
            money_per_day += 20
            wins_per_day += 1
            wins += 1
        elif result == "lose":
            loses_per_day += 1
            loses += 1
    sport = input()

if wins > loses:
    money_sum *= 1.2
    print(f"You won the tournament! Total raised money: {money_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_sum:.2f}")