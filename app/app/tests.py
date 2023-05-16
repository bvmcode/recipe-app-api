""""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        "Test add numbers."
        res = calc.add(2,3)
        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        "Test subtract numbers."
        res = calc.subtract(3,2)
        self.assertEqual(res, 1)
