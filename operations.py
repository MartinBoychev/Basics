num1 = int(input())
num2 = int(input())
operator = input()

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        if (num1 + num2) % 2 == 0:
            print(f"{num1} {operator} {num2} = {num1 + num2} - even")
        else:
            print(f"{num1} {operator} {num2} = {num1 + num2} - odd")
    elif operator == "-":
        if (num1 - num2) % 2 == 0:
            print(f"{num1} {operator} {num2} = {num1 - num2} - even")
        else:
            print(f"{num1} {operator} {num2} = {num1 - num2} - odd")
    if operator == "*":
        if (num1 * num2) % 2 == 0:
            print(f"{num1} {operator} {num2} = {num1 * num2} - even")
        else:
            print(f"{num1} {operator} {num2} = {num1 * num2} - odd")
elif operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} / {num2} = {(num1 / num2):.2f}")
elif operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} % {num2} = {num1 % num2}")