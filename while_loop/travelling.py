destination = input()
budget = float(input())
sum_savings = 0
next_destination_available = False

while destination != "End":
    savings = float(input())
    sum_savings += savings
    next_destination_available = False
    if sum_savings >= budget:
        print(f"Going to {destination}!")
        next_destination_available = True
    if next_destination_available:
        destination = input()
        if destination == "End":
            break
        sum_savings = 0
        budget = float(input())