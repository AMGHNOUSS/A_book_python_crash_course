import calc
import unittest

class Testcalc(unittest.TestCase):
    """class testing"""

    def test_add(self):
        """function testing subtract"""
        self.assertEqual(calc.add(15, 15), 30)
        self.assertEqual(calc.add(-15, 15), 0)
        self.assertEqual(calc.add(-15, -15), -30)
    
    def test_subtract(self):
        """function testing add"""
        self.assertEqual(calc.subtract(15, 15), 0)
        self.assertEqual(calc.subtract(-15, 15), -30)
        self.assertEqual(calc.subtract(-15, -15), 0)
    
    def test_multiply(self):
        """function testing multiply"""
        self.assertEqual(calc.multiply(15, 15), 225)
        self.assertEqual(calc.multiply(-15, 15), -225)
        self.assertEqual(calc.multiply(-15, -15), 225)
    
    def test_divide(self):
        """function testing divide"""
        self.assertEqual(calc.divide(15, 15), 1)
        self.assertEqual(calc.divide(-15, 15), -1)
        self.assertEqual(calc.divide(-15, -15), 1)

        self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)