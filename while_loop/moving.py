width_room = int(input())
length_room = int(input())
height_room = int(input())

full_capacity_room = width_room * length_room * height_room
capacity_left = full_capacity_room
no_more_capacity = False
input_line = input()

while input_line != "Done":
    boxes = int(input_line)
    capacity_left -= boxes

    if capacity_left <= 0:
        no_more_capacity = True
        break
    input_line = input()

if no_more_capacity:
    print(f"No more free space! You need {-capacity_left} Cubic meters more.")
else:
    print(f"{capacity_left} Cubic meters left.")