width_room = int(input())
length_room = int(input())
height_room = int(input())

full_capacity_room = width_room * length_room * height_room
boxes = ""
capacity_left = full_capacity_room

while boxes != "Done":
    boxes = input()
    if boxes == "Done":
        break
    capacity_left -= int(boxes)

    if capacity_left <= 0:
        break

if capacity_left < 0:
    print(f"No more free space! You need {-capacity_left} Cubic meters more.")
else:
    print(f"{capacity_left} Cubic meters left.")