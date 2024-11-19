from unit_factory import UnitFactory
from orc_cavalry import OrcCavalary
from orc_infantry import OrcInfantry

class OrcUnitFactory(UnitFactory):

    def create_infantry(self):
        return OrcInfantry()
    
    def create_cavalry(self):
        return OrcCavalary()