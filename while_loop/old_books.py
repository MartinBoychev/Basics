favourite_book = input()
book_found = False
count_books = 0
book = input()

while book != "No More Books":
    if book == favourite_book:
        book_found = True
        break

    count_books += 1
    book = input()
if book_found:
    print(f"You checked {count_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")
