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
import pandas as pd
#facing issues in my system with imports
import sys
sys.path.append('/Users/whamsy/Documents/asset-allocation')

from assetallocation import generate_portfolios
from assetallocation import functions

file_name = "./Data/SP500.csv"


class UnitTests(unittest.TestCase):
    """Set of unittests for the functions and generate_portfilios
     modules.

    Each function in this class is a self contained unittest.
    All queries necessary for execution are run inside the functions
    without using and global results or variables.
    """
    
    def test_check_key(self):
        """Tests if get_graph_data returns a tuple of 3 elements """
        out = generate_portfolios.get_graph_data(2014, 2018)
        self.assertEqual(len(out), 3)

    def test_date_time_indices(self):
        """check if index is a DateTime index

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected columns encountered.

        Raises:
            Raises AssertionError: Lists differ
        """
        # file_name = "./Data/SP500.csv"
        df_to_test = functions.invest_dataframe(file_name)
        self.assertEqual(type(df_to_test.index), pd.core.indexes.datetimes.DatetimeIndex)

    def test_num_rows(self):
        """check if number of records is as expected.
        We are using the fact that each date occurs only once.
        So number of records should be the number of unique 
        date_time indices.
        
        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected num_rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        # file_name = "./Data/SP500.csv"
        df_to_test = functions.invest_dataframe(file_name)
        rows_to_have = df_to_test.index.nunique()
        self.assertEqual(len(df_to_test), rows_to_have)
    
    def test_num_rows_portfolio(self):
        """check if number of records is as expected.
        We are using the fact that each date occurs only once.
        So number of records should be the number of unique 
        date_time indices.
        
        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected num_rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        stock = functions.invest_dataframe('./Data/SP500.csv')
        bond = functions.invest_dataframe('./Data/BAMLCC0A1AAATRIV.csv')
        stockshare = 0.7
        alloc = [(stock, stockshare), (bond, 1 - stockshare)]
        start = pd.Timestamp(str(2016) + '-01-02 00:00:00', tz=None)
        end = pd.Timestamp(str(2018) + '-01-03 00:00:00', tz=None)
        x = functions.track_portfolio(10000, alloc, 90, start, end)
        rows_to_have = x.index.nunique()
        self.assertEqual(len(x), rows_to_have)
    
    def test_return_rate(self):
        """.
        
        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected num_rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        # file_name = "./Data/SP500.csv"
        df_to_test = functions.invest_dataframe(file_name)
        start = pd.Timestamp(str(2016) + '-01-02 00:00:00', tz=None)
        end = pd.Timestamp(str(2018) + '-01-03 00:00:00', tz=None)
        rate_of_return_percent = functions.calc_return(df_to_test,start,end,kind='percent',annualize=True)
        self.assertGreaterEqual(rate_of_return_percent, 0)
        self.assertLessEqual(rate_of_return_percent,100)



SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
