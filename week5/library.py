#REWRITE USING SOLID PRINCIPALS


class Library:

    def __init__(self):
        self.__books = []
        self.__patrons = []
        self.__transactions = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        self.__books.remove(book)

    def add_patrons(self, patron):
        self.__patrons.append(patron)

    def remove_patrons(self, patron):
        self.__patrons.remove(patron)

    def lend_book(self, book, patron):
        if book in self.__books and patron in self.__patrons:
            self.__transactions.append((book, patron))
            self.__books.remove(book)
            return True
        return False 
    
    def return_book(self, book):
        for transaction in self.__transactions:
            if transaction[0] == book:
                self.__books.append(book)
                self.__transactions.remove(transaction)
                return True
        return False