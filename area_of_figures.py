import math

shape = str(input())

if shape == "square":
    size_1 = float(input())
    area = size_1 * size_1
    print(area)
elif shape == "rectangle":
    size_1 = float(input())
    size_2 = float(input())
    area = size_1 * size_2
    print(area)
elif shape == "circle":
    size_1 = float(input())
    area = math.pi * size_1*size_1
    print("%.3f" % area)
elif shape == "triangle":
    size_1 = float(input())
    size_2 = float(input())
    area = size_1 * size_2 / 2
    print(area)
else:
    print("Please enter valid shape and sizes")




