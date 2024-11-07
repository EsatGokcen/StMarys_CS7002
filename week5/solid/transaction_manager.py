from book import Book
from patron import Patron
from transaction import Transaction

class TransactionManager(Transaction):

    def __init__(self, book : Book, patron : Patron):
        super().__init__(book, patron)
        self.__transactions = []

    def lend_book(self, book : Book):
        for transaction in self.__transactions:
            if transaction.book == book:
                self.__transactions.append(transaction)
                break

    def return_book(self, book : Book):
        for transaction in self.__transactions:
            if transaction.book == book:
                self.__transactions.remove(transaction)
                break