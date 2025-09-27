class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        return [book for book in self.books if book.title == title][0]

b1 = Book("asd","Asd")
b2 = Book("bsd","Bsd")
b3 = Book("csd","Csd")
l = Library([b1, b2, b3])
print(l.find_book("asd"))
