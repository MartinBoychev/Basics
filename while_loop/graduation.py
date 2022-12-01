name = input()
year = 0
total_grade = 0
fails = 0

while True:
    grade = float(input())
    year += 1
    if grade < 4:
        fails += 1
        if fails == 2:
            print(f"{name} has been excluded at {year} grade")
            break
        year -= 1
    else:
        total_grade += grade

    if year == 12:
        avg = total_grade / 12
        print(f"{name} graduated. Average grade: {avg:.2f}")
        break
