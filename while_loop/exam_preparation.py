bad_grades = int(input())
name_of_test = input()

last_problem = ""
total_grades = 0
count_grades = 0
failures = 0
failed = False

while name_of_test != "Enough":
    problem_name = name_of_test
    grade = int(input())

    if grade <= 4:
        failures += 1

    if failures == bad_grades:
        failed = True
        break

    total_grades += grade
    count_grades += 1
    last_problem = name_of_test
    name_of_test = input()

if failed:
    print(f"You need a break, {failures} poor grades.")
else:
    avg = total_grades / count_grades
    print(f"Average score: {avg:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")