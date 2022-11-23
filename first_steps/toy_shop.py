excursion = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_amount = (puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2)
quantity_toys = puzzles + dolls + bears + minions + trucks

if quantity_toys > 49:
    total_discount = total_amount - (total_amount * 0.25)
else:
    total_discount = total_amount

final_money = (total_discount - (total_discount * 0.1)) - excursion


if final_money > -1:
    print(f"Yes!{final_money: .2f} lv left.")
else:
    print(f"Not enough money!{-final_money: .2f} lv needed.")