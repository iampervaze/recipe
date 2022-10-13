"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc

class ClacTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(5,7)
        self.assertEqual(res, 12)
    
    def test_subtract_numbers(self):
        res = calc.subtract(5,3)
        self.assertEqual(res, 2)
