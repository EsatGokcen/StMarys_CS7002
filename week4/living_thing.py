
class LivingThing():

    MAX_ENERGY = 100

    def __init__(self, name, energy, age):
        self.__name = name
        self.__energy = energy
        self.__age = age

    def __repr__(self):
        return f'LivingThing(name={self.__name} , age={self.__age} , energy={self.__energy})'
    
    def __str__(self):
        return f'{self.__name} is {self.__age} years old and has {self.__energy} energy.'
    
    def grow(self):
        did_grow = False
        grow_cost = 50

        if self.__energy >= grow_cost:
            self.__age +=1
            self.__energy -= grow_cost
            did_grow = True

        return did_grow
        

    def reproduce(self):
        energy_required = 20
        did_repro = False

        if self.__energy >= energy_required:
            self.__energy - energy_required
            did_repro = True
        else: 
            did_repro = False

        return did_repro