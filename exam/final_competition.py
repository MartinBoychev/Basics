dancers = int(input())
points = float(input())
season = input()
place = input()
money = 0
charity = 0

if place == "Bulgaria":
    money = points * dancers
    if season == "summer":
        money *= 0.95
    elif season == "winter":
        money *= 0.92
elif place == "Abroad":
    money = (points * dancers) * 1.5
    if season == "summer":
        money *= 0.90
    elif season == "winter":
        money *= 0.85

charity = money * 0.75
amount_left = money * 0.25

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {amount_left / dancers:.2f}")
