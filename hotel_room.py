month = input()
days = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if days > 14:
        studio_price *= 0.7
    elif days > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.7
    if days > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if days > 14:
    apartment_price *= 0.9

print(f"Apartment: {(days * apartment_price):.2f} lv.")
print(f"Studio: {(days * studio_price):.2f} lv.")