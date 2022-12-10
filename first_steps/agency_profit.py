name = input()
adult = float(input())
kids = int(input())
price_adult = float(input())
price_kids = price_adult * 0.3
tax = float(input())

total_kids = (price_kids + tax) * kids
total_adults = (price_adult + tax) * adult
profit = (total_kids + total_adults) * 0.2

print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")