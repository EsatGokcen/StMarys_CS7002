from clothing import Clothing
from week4 import animal as a

class Human(a.Animal):
    MAX_ENERGY = 100
    COST_MOVE = 1

    def __init__(self,name,energy=100,age=0):
        self.__name = name
        self.__age = age
        self.__energy = energy

    def __repr__(self):
        return f'human(name={self.__name}, age={self.__age}, energy={self.__energy})'
    
    def __str__(self):
        return f'{self.__name} is {self.__age} years old and has {self.__energy} energy.'
    
    def grow(self):
        self.__age += 1

    def eat(self, amount):

        self.__energy += amount

        if self.__energy > Human.MAX_ENERGY:
            excess_amount = self.__energy - Human.MAX_ENERGY
        elif self.__energy < Human.MAX_ENERGY:
            excess_amount = self.__energy - Human.MAX_ENERGY
        else:
            excess_amount = 0

        return excess_amount
    
    def reproduce(self):
        energy_required = 20
        did_repro = False

        if self.__energy >= energy_required:
            self.__energy - energy_required
            did_repro = True
        else: 
            did_repro = False

        return did_repro
    
    def move(self, distance):
        did_move = False
        energy_req = distance * Human.COST_MOVE

        if self.__energy >= energy_req:
            did_move = True
        else:
            did_move = False

        return did_move
    
    def dress(self, clothing:Clothing) -> None: #ASK PRINS 
        pass

    def undress(self, clothing:Clothing) -> None: #ASK PRINS 
        pass
    


