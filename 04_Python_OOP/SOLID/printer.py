class Book:
    def __init__(self, content,author, title):
        self.content = content
        self.author = author
        self.title= title


class Formatter:
    def format(self, book):
        return book.content

class PreFormated:
    def format(self, book):
        return book.title

class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book):
        formatted_book = self.formatter.format(book)
        return formatted_book

f = Formatter()
pf = PreFormated()
b1 = Book("asd,", "1", "1")
b2 = Book("bsd,", "2", "2")
p = Printer(pf)
print(p.get_book(b1))