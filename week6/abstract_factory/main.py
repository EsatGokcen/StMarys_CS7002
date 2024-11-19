from human_factory import HumanUnitFactory
from orc_factory import OrcUnitFactory

def main():
    
    def create_units(factory):
        infantry = factory.create_infantry() # ERROR: TypeError: OrcUnitFactory.create_infantry() missing 1 required positional argument: 'self'
        cavalry = factory.create_cavalry()
        print(infantry.sword_attack())
        print(infantry.shield_block())
        print(cavalry.charge())
        print(cavalry.lance_attack())

    human = HumanUnitFactory()
    orc = OrcUnitFactory

    create_units(human)
    create_units(orc)

if __name__ == '__main__':
    main()