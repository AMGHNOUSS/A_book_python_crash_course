
import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    """Class testing"""


    def test_email(self):
        """Testimg Email"""
        em1 = Employee("John", "Bourne", 4000)
        em2 = Employee("Jane", "Smith", 5000)

        self.assertEqual(em1.email, "John.Bourne@email.com")
        self.assertEqual(em2.email, "Jane.Smith@email.com")

        em1.first = 'David'
        em2.first = 'Lara'

        self.assertEqual(em1.email, "David.Bourne@email.com")
        self.assertEqual(em2.email, "Lara.Smith@email.com")
    

    def test_fullname(self):
        """Testing Full name"""
        
        em1 = Employee("John", "Bourne", 4000)
        em2 = Employee("Jane", "Smith", 5000)

        self.assertEqual(em1.fullname, "John Bourne")
        self.assertEqual(em2.fullname, "Jane Smith")

        em1.first = 'David'
        em2.first = 'Lara'

        self.assertEqual(em1.fullname, "David Bourne")
        self.assertEqual(em2.fullname, "Lara Smith")
    
    def test_raise(self):
        """Testing raise"""
        em1 = Employee("John", "Bourne", 4000)
        em2 = Employee("Jane", "Smith", 5000)

        em1.apply_raise()
        em2.apply_raise()

        self.assertEqual(em1.pay, 4200)
        self.assertEqual(em2.pay, 5250)