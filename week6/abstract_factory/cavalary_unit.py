from abc import ABC, abstractmethod

class CavalaryUnit(ABC):

    @abstractmethod
    def charge(self):
        pass

    @abstractmethod
    def lance_attack(self):
        pass