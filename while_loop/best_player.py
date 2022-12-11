import sys
name = input()

best_pl = ""
max_goals = -sys.maxsize
hattrick = 0

while name != "END":
    goals = int(input())
    if goals > max_goals:
        best_pl = name
        max_goals = goals
        if goals >= 3:
            hattrick = 1
        if goals >= 10:
            break

    name = input()

print(f"{best_pl} is the best player!")
if hattrick == 1:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")