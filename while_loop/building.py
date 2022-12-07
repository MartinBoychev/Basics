
floors = int(input())
rooms = int(input())

sign = ""
flat_num = 0

for fl in range(floors, 0, -1):
    for r in range(rooms):

        flat_num = fl * 10 + r

        if fl == floors:
            r = f"L{flat_num}"
        elif fl % 2 == 0:
            r = f"O{flat_num}"
        elif fl % 2 != 0:
            r = f"A{flat_num}"
        print(r, end=" ")
    print()