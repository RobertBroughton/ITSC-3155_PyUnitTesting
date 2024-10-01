import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 2), 4)
        self.assertEqual(Calculator.add(1, 1), 2)
    def test_subtract(self):
        self.assertEqual(Calculator.subtract(2, 2), 0)
        self.assertEqual(Calculator.subtract(1, 1), 0)
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 2), 4)
        self.assertEqual(Calculator.multiply(1, 1), 1)
    def test_divide(self):
        self.assertEqual(Calculator.divide(2, 2), 1)
        self.assertEqual(Calculator.divide(4, 2), 2)

if __name__ == '__main__':
    unittest.main()