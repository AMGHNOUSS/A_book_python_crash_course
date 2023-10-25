
import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    """Class testing"""

    def setUp(self):
        self.em1 = Employee("John", "Bourne", 4000)
        self.em2 = Employee("Jane", "Smith", 5000)
    
    def tearDown(self):
        """tearDown"""

    def test_email(self):
        """Testimg Email"""
        
        self.assertEqual(self.em1.email, "John.Bourne@email.com")
        self.assertEqual(self.em2.email, "Jane.Smith@email.com")

        self.em1.first = 'David'
        self.em2.first = 'Lara'

        self.assertEqual(self.em1.email, "David.Bourne@email.com")
        self.assertEqual(self.em2.email, "Lara.Smith@email.com")
    

    def test_fullname(self):
        """Testing Full name"""

        self.assertEqual(self.em1.fullname, "John Bourne")
        self.assertEqual(self.em2.fullname, "Jane Smith")

        self.em1.first = 'David'
        self.em2.first = 'Lara'

        self.assertEqual(self.em1.fullname, "David Bourne")
        self.assertEqual(self.em2.fullname, "Lara Smith")
    
    def test_raise(self):
        """Testing raise"""
        self.em1.apply_raise()
        self.em2.apply_raise()

        self.assertEqual(self.em1.pay, 4200)
        self.assertEqual(self.em2.pay, 5250)