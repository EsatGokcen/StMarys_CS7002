
class Patron:

    next_patron_id = 1000

    def __init__(self, name):
        self.__name = name
        self.__id = Patron.next_patron_id
        Patron.next_patron_id += 1

        self.__patrons = []

    def __repr__(self):
        return f'Patron(name={self.__name} , id={self.__id})'
    
    def __str__(self):
        return f'Patron name: {self.__name} \nPatron id: {self.__id}'
    