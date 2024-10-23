#NOT MODIFIED - NEED TO MAKE IT SPECIFIC TO CLASS BEING TESTED

import unittest
from venus_flytrap import VenusFlyTrap   # type: ignore

class HumanTestCase(unittest.TestCase):

    def test_eat(self):
        #Energy is full and try to eat
        human_esat = VenusFlyTrap("Esat")
        self.assertEqual(human_esat.eat(20), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_esat = VenusFlyTrap("Esat" , energy = 90)
        self.assertEqual(human_esat.eat(20), 10, "Excess should be 20.")

        #energy is below 100 and eat exactly what is required
        human_esat = VenusFlyTrap("Esat" , energy = 80)
        self.assertEqual(human_esat.eat(20), 0, "Excess should be 0.")

        #energy is below 100 and eat less than required
        human_esat = VenusFlyTrap("Esat" , energy = 70)
        self.assertEqual(human_esat.eat(20), -10, "Excess should be -10.")

    #add additional tests here


if __name__ == '__main__':
    unittest.main()