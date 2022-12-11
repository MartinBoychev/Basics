import math

num_balls = int(input())
points = 0
red = 0
yellow = 0
orange = 0
white = 0
black = 0
other = 0



for _ in range(num_balls):
    color = input()
    if color == "red":
        points += 5
        red += 1
    elif color == "orange":
        points += 10
        orange += 1
    elif color == "yellow":
        points += 15
        yellow += 1
    elif color == "white":
        points += 20
        white += 1
    elif color == "black":
        points = points / 2
        points = math.floor(points)
        black += 1
    else:
        other += 1

print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")
