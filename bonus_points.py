number = int(input())
bonus = 0

if number < 100:
    bonus += 5
elif 1000 > number > 100:
    bonus = 0.2 * number
elif number > 1000:
    bonus = 0.1 * number
else:
    print("Write valid number")

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2
else:
    print("Write valid number")

print(bonus)
print(bonus + number)

