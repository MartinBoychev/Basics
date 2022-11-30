length_cake = int(input())
width_cake = int(input())

size_cake = length_cake * width_cake
count_pieces = size_cake

while size_cake > 0:
    cutting_cake = input()

    if cutting_cake == "STOP":
        break

    count_pieces = abs(size_cake - int(cutting_cake))
    size_cake -= int(cutting_cake)

if size_cake >= 0:
    print(f"{count_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {count_pieces} pieces more.")