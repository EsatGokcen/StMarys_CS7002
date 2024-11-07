from book import Book

class BookRepository:

    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book : Book):
        self.__books.remove(book)

    def __str__(self):
        books = "Books' List: " + "\n".join(self.__books)
        return books