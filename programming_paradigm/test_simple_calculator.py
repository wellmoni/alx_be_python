import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator =SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,3)2)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,4)16)
    def test_divide(self):
        self.assertEqual(self.calc.divide(4,1)4)

