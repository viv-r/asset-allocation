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

import sys
import os
import inspect
import unittest
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
GPARENT_DIR = os.path.dirname(PARENT_DIR)

sys.path.insert(0, GPARENT_DIR)

from assetallocation import generate_portfolios, functions

FILE_NAME = "./Data/SP500.csv"


class UnitTests(unittest.TestCase):
    """Set of unittests for the functions and generate_portfolios
     modules.

    Each function in this class is a self contained unittest.
    All queries necessary for execution are run inside the functions
    without using and global results or variables.
    """

    # def test_check_key(self):
    #     """Tests if get_graph_data returns a tuple of 3 elements """
    #     out = generate_portfolios.get_graph_data(2014, 2018)
    #     self.assertEqual(len(out), 3)

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
        df_to_test = functions.invest_dataframe(FILE_NAME)
        self.assertEqual(type(df_to_test.index), pd.core.indexes.datetimes.DatetimeIndex)

    def test_num_rows_with_data(self):
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
        len_file = 0
        with open(FILE_NAME) as f:
            for i, l in enumerate(f):
                len_file += 1
        df_to_test = functions.invest_dataframe(FILE_NAME)
        rows_output = df_to_test.index.shape[0]
        self.assertGreater(rows_output, len_file)
    
    def test_file_name(self):
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
        df_to_test = functions.invest_dataframe(FILE_NAME)
        out_file_name = list(df_to_test)[0]
        c1 = "/"
        c2 = "."
        break1 = [pos for pos, char in enumerate(FILE_NAME) if char == c1]
        break2 = [pos for pos, char in enumerate(FILE_NAME) if char == c2]
        in_file_name = FILE_NAME[break1[-1]+1:break2[-1]]
        self.assertEqual(in_file_name, out_file_name)
    
    
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
        df_to_test = functions.invest_dataframe(FILE_NAME)
        rows_to_have = df_to_test.index.nunique()
        self.assertEqual(len(df_to_test), rows_to_have)
    
    def test_calc_return_type(self):
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
        data_input = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp('1990-01-02 00:00:00', tz=None)
        end = pd.Timestamp('2018-01-03 00:00:00', tz=None)
        out_return = functions.calc_return(data_input,start,end)
        self.assertEqual(float, type(out_return))

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
        x_portfolio = functions.track_portfolio(10000, alloc, 90, start, end)
        rows_to_have = x_portfolio.index.nunique()
        self.assertEqual(len(x_portfolio), rows_to_have)

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
        df_t = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp(str(2016) + '-01-02 00:00:00', tz=None)
        end = pd.Timestamp(str(2018) + '-01-03 00:00:00', tz=None)
        ror_percent = functions.calc_return(df_t, start, end, return_type='percent', annualize=True)
        self.assertGreaterEqual(ror_percent, 0)
        self.assertLessEqual(ror_percent, 100)

    def test_risk_return(self):
        """


        """
        



SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
