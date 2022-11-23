turns = int(input())
invalid = 0
zero_to_9 = 0
ten_to_19 = 0
twenty_to_29 = 0
thirty_to_39 = 0
forty_to_49 = 0

result = 0

for _ in range(0, turns):
    number = int(input())
    if number < 0 or 50 < number:
        invalid += 1
        result /= 2
    elif number < 10:
        zero_to_9 += 1
        result += (0.2 * number)
    elif number < 20:
        ten_to_19 += 1
        result += (0.3 * number)
    elif number < 30:
        twenty_to_29 += 1
        result += (0.4 * number)
    elif number < 40:
        thirty_to_39 += 1
        result += 50
    elif number <= 50:
        forty_to_49 += 1
        result += 100

print(f"{result:.2f}")
print(f"From 0 to 9: {zero_to_9 / turns * 100:.2f}%")
print(f"From 10 to 19: {ten_to_19 / turns * 100:.2f}%")
print(f"From 20 to 29: {twenty_to_29 / turns * 100:.2f}%")
print(f"From 30 to 39: {thirty_to_39 / turns * 100:.2f}%")
print(f"From 40 to 50: {forty_to_49 / turns * 100:.2f}%")
print(f"Invalid numbers: {invalid / turns * 100:.2f}%")