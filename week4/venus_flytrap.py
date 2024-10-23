
from plant import Plant
from animal import Animal

class VenusFlyTrap(Plant):

    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return super().__repr__()
    
    def __str__(self):
        return super().__str__()
    
    def catch(self, insect):
        if insect == Animal(self.__name):
            Plant.absorb()
    

    