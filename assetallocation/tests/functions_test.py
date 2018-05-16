"""
This file contains test cases for the functions
defined generate_portfolios.py

Classes:
    UnitTests: Class containing test cases

Functions:
    None.
Exceptions:
    None.
"""

import unittest
from assetallocation import generate_portfolios


class UnitTests(unittest.TestCase):
    def test_check_key(self):
        """Tests if get_graph_data returns a tuple of 3 elements """
        out = generate_portfolios.get_graph_data(2014, 2018)
        self.assert(len(out) == 3)


SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
