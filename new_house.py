type_flowers = input()
count_flowers = int(input())
budget = int(input())

final_price = 0

if type_flowers == "Roses":
    final_price = count_flowers * 5
    if count_flowers > 80:
        final_price = final_price * 0.9
elif type_flowers == "Dahlias":
    final_price = (count_flowers * 3.8)
    if count_flowers > 90:
        final_price *=  0.85
elif type_flowers == "Tulips":
    final_price = count_flowers * 2.8
    if count_flowers > 80:
        final_price *= 0.85
elif type_flowers == "Narcissus":
    final_price = count_flowers * 3
    if count_flowers < 120:
        final_price *= 1.15
elif type_flowers == "Gladiolus":
    final_price = count_flowers * 2.5
    if count_flowers < 80:
        final_price *= 1.2

if budget >= final_price:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {(budget - final_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(final_price - budget):.2f} leva more.")