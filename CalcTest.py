import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.operate(2, 3, "add"), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.operate(5, 2, "sub"), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.operate(4, 3, "mul"), 12)

    def test_divide(self):
        self.assertEqual(self.calc.operate(10, 2, "div"), 5.0)
        with self.assertRaises(ValueError):
            self.calc.operate(5, 0, "div")

if __name__ == "__main__":
    unittest.main()