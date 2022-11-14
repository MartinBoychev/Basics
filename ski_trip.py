days = int(input())
room = input()
review = input()
price_one_pers = 18
price_apart = 25
price_pres_apart = 35

nights = days - 1
price = 0

if room == "room for one person":
    price = price_one_pers * nights
elif room == "apartment":
    if nights < 10:
        price = (price_apart * nights) * 0.7
    elif nights <= 15:
        price = (price_apart * nights) * 0.65
    else:
        price = (price_apart * nights) * 0.5
elif room == "president apartment":
    if nights < 10:
        price = (price_pres_apart * nights) * 0.9
    elif nights <= 15:
        price = (price_pres_apart * nights) * 0.85
    else:
        price = (price_pres_apart * nights) * 0.8

if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.9
print(f"{price:.2f}")
