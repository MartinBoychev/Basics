count = int(input())
type_frame = input()
del_or_not = input()

price = 0

if count < 10:
    print("Invalid order")
else:
    if type_frame == "90X130":
        price = count * 110
        if 30 < count < 61:
            price = price - (price * 0.05)
        elif count > 60:
            price = price - (price * 0.08)
    elif type_frame == "100X150":
        price = count * 140
        if 40 < count < 81:
            price = price - (price * 0.06)
        elif count > 80:
            price = price - (price * 0.1)
    elif type_frame == "130X180":
        price = count * 190
        if 20 < count < 51:
            price = price - (price * 0.07)
        elif count > 50:
            price = price - (price * 0.12)
    elif type_frame == "200X300":
        price = count * 250
        if 25 < count < 51:
            price = price - (price * 0.09)
        elif count > 50:
            price = price - (price * 0.14)
    if del_or_not == "With delivery":
        price += 60
    if count > 99:
        price = price - (price * 0.04)

    print(f"{price:.2f} BGN")