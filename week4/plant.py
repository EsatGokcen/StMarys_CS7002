from living_thing import LivingThing

class Plant(LivingThing):

    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f'Plant(name={self.__name} , energy={self.__energy})'
    
    def __str__(self):
        return f'{self.__name} is a plant with {self.__energy} energy.'
    
    def absorb(self, amount):
        self.__energy += amount

        if self.__energy > Plant.MAX_ENERGY:
            excess_amount = self.__energy - Plant.MAX_ENERGY
        elif self.__energy < Plant.MAX_ENERGY:
            excess_amount = self.__energy - Plant.MAX_ENERGY
        else:
            excess_amount = 0

        return excess_amount