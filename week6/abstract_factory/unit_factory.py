from abc import ABC, abstractmethod

class UnitFactory(ABC):

    @abstractmethod
    def create_infantry(self):
        pass

    @abstractmethod
    def create_cavalry(self):
        pass