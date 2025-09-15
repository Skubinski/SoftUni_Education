shelf_with_books = input().split('&')
while True:
    command = input().split(" | ")
    if command[0] == 'Done':
        break
    elif command[0] == "Add Book":
        if not command[1] in shelf_with_books:
            shelf_with_books.insert(0, command[1])
    elif command[0] == "Take Book":
        if command[1] in shelf_with_books:
            shelf_with_books.remove(command[1])
    elif command[0] == "Swap Books":
        if command[1] in shelf_with_books and command[2] in shelf_with_books:
            book_1 = command[1]
            book_1_index = shelf_with_books.index(book_1)
            book_2 = command[2]
            book_2_index = shelf_with_books.index(book_2)
            shelf_with_books[book_1_index], shelf_with_books[book_2_index] = shelf_with_books[book_2_index], shelf_with_books[book_1_index]
    elif command[0] == "Insert Book":
        if not command[1] in shelf_with_books:
            shelf_with_books.append(command[1])
    elif command[0] == "Check Book":
        index = int(command[1])
        if not index > len(shelf_with_books) and not index < 0:
            print(shelf_with_books[index])
print(', '.join(shelf_with_books))