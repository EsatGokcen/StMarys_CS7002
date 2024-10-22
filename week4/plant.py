from living_thing import LivingThing

class Plant(LivingThing):

    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f''
    
    def __str__(self):
        return f''
    
    def absorb(self, amount):
        self.__energy += amount

        if self.__energy > Plant.MAX_ENERGY:
            excess_amount = self.__energy - Plant.MAX_ENERGY
        elif self.__energy < Plant.MAX_ENERGY:
            excess_amount = self.__energy - Plant.MAX_ENERGY
        else:
            excess_amount = 0

        return excess_amount