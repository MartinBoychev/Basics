capacity = float(input())
cargo_load = 0
count_suitcases = 0
action = input()

while action != "End":
    suitcase = float(action)
    count_suitcases += 1
    if count_suitcases % 3 == 0:
        cargo_load += suitcase * 1.1
    else:
        cargo_load += suitcase
    if capacity < cargo_load:
        count_suitcases -= 1
        print("No more space!")
        break
    action = input()

if action == "End":
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {count_suitcases} suitcases loaded.")