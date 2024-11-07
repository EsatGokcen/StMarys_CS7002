from book_repository import BookRepository
from patron_repository import PatronRepository
from transaction_manager import TransactionManager


class Library:

    def __init__(self, book_repo : BookRepository, patron_repo : PatronRepository, transaction_manager : TransactionManager):
        self.__book_repo = book_repo
        self.__patron_repo = patron_repo
        self.__transaction_manager = transaction_manager

    def lend_book(self, book, patron):
        if book in self.__book_repo.books and patron in self.__patron_repo.patrons:
            self.__transaction_manager.lend_book(book, patron)
            self.__book_repo.remove_book(book)
            return True
        else:
            return False
        
    def return_book(self, book):
        self.__transaction_manager.return_book(book)
        self.__book_repo.add_book(book)