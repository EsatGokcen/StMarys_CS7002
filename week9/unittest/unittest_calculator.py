import unittest
from simple_calculator import Calculator

class TestCalculator(unittest.TestCase):

    def set_up(self):
        self.calculator = Calculator()

    def test_add(self):
        actual = self.calculator.add(5,3)
        expectation = 8
        self.assertEqual(actual, expectation)