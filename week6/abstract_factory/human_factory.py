from unit_factory import UnitFactory
from human_cavalry import HumanCavalary
from human_infantry import HumanInfantry

class HumanUnitFactory(UnitFactory):

    def create_infantry(self):
        return HumanInfantry()
    
    def create_cavalry(self):
        return HumanCavalary()