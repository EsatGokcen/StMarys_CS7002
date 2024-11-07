from patron import Patron

class PatronRepository:

    def __init__(self):
        self.__patrons = []

    def add_patron(self, patron):
        self.__patrons.append(patron)

    def remove_patron(self, patron : Patron):
        self.__patrons.remove(patron)