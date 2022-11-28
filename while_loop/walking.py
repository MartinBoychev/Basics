total_steps = 0
action = input()

while action != "Going home":
    steps_home = int(action)
    total_steps += steps_home
    if total_steps >= 10000:
        break
    action = input()
if action == "Going home":
    last_steps = int(input())
    total_steps += last_steps

if total_steps < 10000:
    print(f"{10000 - total_steps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job! \n{total_steps - 10000} steps over the goal!")