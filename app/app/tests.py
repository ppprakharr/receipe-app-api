from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """test adding numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """testing subtracting numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
