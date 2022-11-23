budget = int(input())
season = input()
count_fishermen = int(input())

price_of_boat = 0

if season == "Spring":
    price_of_boat = 3000
    if count_fishermen <=6:
        price_of_boat *= 0.9
    elif count_fishermen < 12:
        price_of_boat *= 0.85
    else:
        price_of_boat *= 0.75
elif season == "Summer" or season == "Autumn":
    price_of_boat = 4200
    if count_fishermen <=6:
        price_of_boat *= 0.9
    elif count_fishermen < 12:
        price_of_boat *= 0.85
    else:
        price_of_boat *= 0.75
elif season == "Winter":
    price_of_boat = 2600
    if count_fishermen <=6:
        price_of_boat *= 0.9
    elif count_fishermen < 12:
        price_of_boat *= 0.85
    else:
        price_of_boat *= 0.75

if (count_fishermen % 2) == 0 and season != "Autumn":
    price_of_boat *= 0.95

diff = abs(budget - price_of_boat)

if budget >= price_of_boat:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")