"""
This file contains test cases for the functions
defined in backend/functions.py

Classes:
    UnitTests: Class containing  all the test cases
Functions:
    Different types of unittest cases.
Exceptions:
    None.
"""

import sys
import os
import inspect
import unittest
import pandas as pd
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
FINAL_DIR = os.path.join(str(PARENT_DIR), "assetallocation")
sys.path.insert(0, PARENT_DIR)
sys.path.insert(0, FINAL_DIR)

#pylint: disable=wrong-import-position
from backend import functions
#pylint: enable=wrong-import-position
FILE_NAME = "./Data/SP500.csv"

class UnitTests(unittest.TestCase):
    """Set of unittests for the functions module.

    Each function in this class is a self contained unittest.
    All queries necessary for execution are run inside the functions
    without using and global results or variables.
    """

    def test_date_time_indices(self):
        """check if index is a DateTime index

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected columns encountered.

        Raises:
            Raises AssertionError: Type not equal
        """
        df_to_test = functions.invest_dataframe(FILE_NAME)
        self.assertEqual(type(df_to_test.index), pd.core.indexes.datetimes.DatetimeIndex)

    def test_num_rows_with_data(self):
        """Check that the number of rows in the dataframe
        returned is greater than the number of rows in the
        input data file.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay
            else raises an error if unexpected number of
            rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        len_file = 0
        #pylint: disable=unused-variable
        with open(FILE_NAME) as file_open:
            for i, el_num in enumerate(file_open):
                len_file += 1
        #pylint: enable=unused-variable
        df_to_test = functions.invest_dataframe(FILE_NAME)
        rows_output = df_to_test.index.shape[0]
        self.assertGreater(rows_output, len_file)

    def test_file_name(self):
        """check if the index of output dataframe has the
        same name as the input file.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected column name encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        df_to_test = functions.invest_dataframe(FILE_NAME)
        out_file_name = list(df_to_test)[0]
        char_one = "/"
        char_two = "."
        break1 = [pos for pos, char in enumerate(FILE_NAME) if char == char_one]
        break2 = [pos for pos, char in enumerate(FILE_NAME) if char == char_two]
        in_file_name = FILE_NAME[break1[-1]+1:break2[-1]]
        self.assertEqual(in_file_name, out_file_name)

    def test_num_rows(self):
        """check if number of records is as expected.
        Since that each date occurs only once, number
        of records should be the number of unique date_time
        indices.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error.

        Raises:
            Raises AssertionError Values not equal
        """
        df_to_test = functions.invest_dataframe(FILE_NAME)
        rows_to_have = df_to_test.index.nunique()
        self.assertEqual(len(df_to_test), rows_to_have)

    def test_calc_return_type(self):
        """check if the value returned by the calc_return
        function is of type float.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if different return type encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        data_input = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp('1990-01-02 00:00:00', tz=None)
        end = pd.Timestamp('2018-01-03 00:00:00', tz=None)
        out_return = functions.calc_return(data_input, start, end)
        self.assertEqual(float, type(out_return))

    def test_return_list_type(self):
        """check if the output of the invest_dataframe function
        is a numpy array (numpy.ndarray).

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected num_rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        data_input = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp('1990-01-02 00:00:00', tz=None)
        end = pd.Timestamp('2018-01-03 00:00:00', tz=None)
        out_return = functions.return_list(data_input, start, end)
        self.assertEqual(np.ndarray, type(out_return))

    def test_return_list_num_rows(self):
        """check if number of rows returned by the return_list
        function is less than or equal to the number of days
        being considered in the calculation.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected num_rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        data_input = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp('1990-01-02 00:00:00', tz=None)
        end = pd.Timestamp('2018-01-03 00:00:00', tz=None)
        out_return = functions.return_list(data_input, start, end)
        num_days_str = str(end - start)
        num_days = int(num_days_str[:num_days_str.find(" ")])
        self.assertLessEqual(out_return.shape[0], num_days)

    def test_calc_risk_return_type(self):
        """check if calc_risk function returns an output
        of type numpy.float64.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected num_rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        data_input = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp('1990-01-02 00:00:00', tz=None)
        end = pd.Timestamp('2018-01-03 00:00:00', tz=None)
        out_return = functions.calc_risk(data_input, start, end)
        self.assertEqual("<class 'numpy.float64'>", str(type(out_return)))

    def test_calc_risk_return_val(self):
        """verify that the output of the calc_risk function is
        greater than or equal to zero.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected value encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        data_input = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp('1990-01-02 00:00:00', tz=None)
        end = pd.Timestamp('2018-01-03 00:00:00', tz=None)
        out_return = functions.calc_risk(data_input, start, end)
        self.assertGreaterEqual(out_return, 0)


    def test_num_rows_portfolio(self):
        """check if track_portfolio returns a number of records
        equal to the number of unique date_time indices.

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
        """check that calc_return gives a valid return rate
        between 0 and 100, when the return_type is percent.

        Args:
            No special arguments as it is a unittest.

        Returns:
            No return values. Passes the test if all okay else
            raises an error if unexpected num_rows encountered.

        Raises:
            Raises AssertionError Values not equal
        """
        df_t = functions.invest_dataframe(FILE_NAME)
        start = pd.Timestamp(str(2016) + '-01-02 00:00:00', tz=None)
        end = pd.Timestamp(str(2018) + '-01-03 00:00:00', tz=None)
        ror_percent = functions.calc_return(df_t, start, end, return_type='percent', annualize=True)
        self.assertGreaterEqual(ror_percent, 0)
        self.assertLessEqual(ror_percent, 100)

SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
