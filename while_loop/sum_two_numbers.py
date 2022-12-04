beginning = int(input())
end_interval = int(input())
magic_num = int(input())

counter = 0
coincidence = False

for i in range(beginning, end_interval + 1):
    for u in range(beginning, end_interval + 1):
        counter += 1
        if i + u == magic_num:
            print(f"Combination N:{counter} ({i} + {u} = {magic_num})")
            coincidence = True
    if coincidence:
        break

if not coincidence:
    print(f"{counter} combinations - neither equals {magic_num}")