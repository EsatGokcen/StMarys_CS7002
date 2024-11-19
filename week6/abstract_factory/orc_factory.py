from unit_factory import UnitFactory

class OrcUnitFactory(UnitFactory):

    def create_infantry(self):
        return "Created orc infantry unit."
    
    def create_cavalry(self):
        return "Created orc cavalary unit."