import math

tournaments = int(input())
starting_points = int(input())

final_points = starting_points
wins = 0
for _ in range(0, tournaments):
    achievement = input()
    if achievement == "W":
        final_points += 2000
        wins += 1
    elif achievement == "F":
        final_points += 1200
    elif achievement == "SF":
        final_points += 720
win_rate = wins / tournaments * 100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor((final_points - starting_points) / tournaments)}")
print(f"{win_rate:.2f}%")