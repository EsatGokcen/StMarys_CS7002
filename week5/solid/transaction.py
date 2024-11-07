from book import Book
from patron import Patron

class Transaction:

    next_transaction_id = 1000

    def __init__(self, book : Book, patron : Patron):
        self.__id = Transaction.next_transaction_id
        Transaction.next_transaction_id += 1
        self.__book = book
        self.__patron = patron

    def __repr__(self):
        return f'Transaction(id={self.__id})'
    
    def __str__(self):
        return f'Transaction id: {self.__id}'
    