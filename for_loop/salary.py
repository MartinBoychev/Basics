open_tabs = int(input())
salary = int(input())
reduced_salary = salary
for i in range (0, open_tabs):
    website = input()
    if website == "Facebook":
        reduced_salary -= 150
    elif website == "Instagram":
        reduced_salary -= 100
    elif website == "Reddit":
        reduced_salary -= 50
    if reduced_salary <= 0:
        break

if reduced_salary <= 0:
    print("You have lost your salary.")
else:
    print(reduced_salary)
