count_students = int(input())

failed = 0
between_3_4 = 0
between_4_5 = 0
top_students = 0
sum_grades = 0

for _ in range(0, count_students):
    grade = float(input())
    if grade < 3:
        failed += 1
        sum_grades += grade
    elif grade < 4:
        between_3_4 += 1
        sum_grades += grade
    elif grade < 5:
        between_4_5 += 1
        sum_grades += grade
    elif grade >= 5:
        top_students += 1
        sum_grades += grade

avg = sum_grades / count_students
print(f"Top students: {top_students / count_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_5 / count_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_4 / count_students * 100:.2f}%")
print(f"Fail: {failed / count_students * 100:.2f}%")
print(f"Average: {avg:.2f}")


