
from week3 import human as h

class SuperHuman(h.Human):

    FLY_COST = 5

    def __init__(self, name, energy=100, age=0):
        super().__init__(name, energy, age)

    def __repr__(self):
        return super().__repr__()
    
    def __str__(self):
        return super().__str__()
    
    def fly(self, distance):
        energy_loss = distance * SuperHuman.FLY_COST

        if self.__energy >= energy_loss:
            return f"{self.__name} has flown {distance}.\Energy loss: {energy_loss}."
        return f"Not enough energy! Energy required: {energy_loss}"



