import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    
    # add sub opeation test
    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(19, 3), 16)

    # add mul operation test
    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(7, 38), 266)

    # add div operation test
    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5.0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()