import calc
import unittest

class Testcalc(unittest.TestCase):
    """class testing"""

    def test_add(self):
        """function testing add"""
        self.assertEqual(calc.add(15, 15), 30)