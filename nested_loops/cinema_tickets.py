name_movie = input()
students = 0
standard = 0
kids = 0
occ_seats = 0
total_tickets = 0

while name_movie != "Finish":
    free_seats = int(input())
    for _ in range(free_seats):
        type_ticket = input()
        if type_ticket == "End":
            break
        occ_seats += 1
        total_tickets += 1
        if type_ticket == "student":
            students += 1
        elif type_ticket == "standard":
            standard += 1
        elif type_ticket == "kid":
            kids += 1

    print(f"{name_movie} - {occ_seats / free_seats*100:.2f}% full.")
    occ_seats = 0
    name_movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{students / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids / total_tickets * 100:.2f}% kids tickets.")
