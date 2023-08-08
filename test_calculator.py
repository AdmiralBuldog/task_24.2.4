import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_multiply(self):
        result = self.calc.multiply(3, 7)
        self.assertEqual(result, 21)

    def test_division(self):
        result = self.calc.division(10, 2)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calc.subtraction(15, 5)
        self.assertEqual(result, 10)

    def test_adding(self):
        result = self.calc.adding(8, 2)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
