searched_book = input()
books_counter = 0
is_found = False
next_book = input()
while next_book != "No More Books":
    if next_book == searched_book:
        is_found = True
        break
    books_counter += 1
    next_book = input()
if is_found:
    print(f'You checked {books_counter} books and found it.')
else:
    print("The book you search is not here!")
    print(f'You checked {books_counter} books.')