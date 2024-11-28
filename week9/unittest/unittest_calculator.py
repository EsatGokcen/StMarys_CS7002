import unittest
from simple_calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        actual = calculator.add(5,3)
        expectation = 8
        self.assertEqual(actual, expectation)