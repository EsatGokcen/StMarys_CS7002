from unit_factory import UnitFactory

class HumanUnitFactory(UnitFactory):

    def create_infantry(self):
        return "Created human infantry unit."
    
    def create_cavalry(self):
        return "Created human cavalry unit."