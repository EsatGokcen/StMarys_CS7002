
from living_thing import LivingThing

class Fungi(LivingThing):

    def __init__(self, name, energy, age):
        super().__init__(name, energy, age)

    def __repr__(self):
        return super().__repr__()
    
    def __str__(self):
        return super().__str__()
    
    def saprotrophic_nutrition(self, amount):

        breakdown = amount * 2
        self.__energy += breakdown

        if self.__energy > Fungi.MAX_ENERGY:
            excess_amount = self.__energy - Fungi.MAX_ENERGY
        elif self.__energy < Fungi.MAX_ENERGY:
            excess_amount = self.__energy - Fungi.MAX_ENERGY
        else:
            excess_amount = 0

        return excess_amount


