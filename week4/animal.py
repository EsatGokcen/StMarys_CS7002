from living_thing import LivingThing

class Animal(LivingThing):

    COST_MOVE = 1

    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f'animal(name={self.__name}, age={self.__age}, energy={self.__energy})'
    
    def __str__(self):
        return f'{self.__name} is {self.__age} years old and has {self.__energy} energy.'
    
    def move(self, distance):
        did_move = False
        energy_req = distance * Animal.COST_MOVE

        if self.__energy >= energy_req:
            did_move = True
        else:
            did_move = False

        return did_move

    def eat(self, amount):
        self.__energy += amount

        if self.__energy > Animal.MAX_ENERGY:
            excess_amount = self.__energy - Animal.MAX_ENERGY
        elif self.__energy < Animal.MAX_ENERGY:
            excess_amount = self.__energy - Animal.MAX_ENERGY
        else:
            excess_amount = 0

        return excess_amount
        
        