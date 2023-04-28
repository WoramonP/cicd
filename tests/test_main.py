"""
Test the main module.
Author: Woramon P.
"""

from unittest import TestCase
from main import multiply_by_two, multiply_by_two_str


class Test(TestCase):
    def test_multiply_by_two(self):
        assert multiply_by_two(5) == 10
        assert multiply_by_two(0) == 0
        assert multiply_by_two(-5) == -10

    def test_multiply_by_two_str(self):
        assert multiply_by_two_str("0") == "0 x 2 equals to 0."
        assert multiply_by_two_str("200") == "200 x 2 equals to 400."
        assert multiply_by_two_str("-1") == "Please enter a positive integer."
        assert multiply_by_two_str("A") == "Please enter a positive integer."
        assert multiply_by_two_str("") == "Please enter a positive integer."
