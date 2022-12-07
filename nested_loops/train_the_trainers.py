n = int(input())
presentation = input()
sum_total_grade = 0
counter = 0

while presentation != "Finish":
    sum_grade = 0

    for i in range(n):
        grade = float(input())
        sum_grade += grade
        sum_total_grade += grade
        counter += 1

    avg = sum_grade / n
    print(f"{presentation} - {avg:.2f}.")
    presentation = input()

avg_final = sum_total_grade / counter
print(f"Student's final assessment is {avg_final:.2f}.")
