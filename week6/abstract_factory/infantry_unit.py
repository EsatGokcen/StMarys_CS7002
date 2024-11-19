from abc import ABC, abstractmethod

class InfantryUnit(ABC):

    @abstractmethod
    def sword_attack(self):
        pass

    @abstractmethod
    def shield_block(self):
        pass

