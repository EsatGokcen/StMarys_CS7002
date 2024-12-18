
class Book:

    def __init__(self, name, author):
        self.__name = name
        self.__author = author

    def __repr__(self):
        return f'Book(name={self.__name}, author={self.__author})'
    
    def __str__(self):
        return f'Book name: {self.__name}, Book author: {self.__author}.'
