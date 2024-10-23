
from living_thing import LivingThing
from flying_super_power import FlyingSuperPower #NO CLUE HOW TO IMPLEMENT
from invisibility_super_power import InvisibilitySuperPower #NO CLUE HOW TO IMPLEMENT

class Alien(LivingThing):

    def __init__(self, name, energy, age):
        super().__init__(name, energy, age)

    def __repr__(self):
        return super().__repr__()
    
    def __str__(self):
        return super().__str__()
    
    FlyingSuperPower.fly()
    InvisibilitySuperPower.invisible()
    InvisibilitySuperPower.visible()


    


    