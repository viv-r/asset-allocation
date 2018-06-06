'''Tests user_input.py module'''
#pylint: disable=duplicate-code
import sys
import os
import inspect
import unittest
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
FINAL_DIR = os.path.join(str(PARENT_DIR), 'assetallocation')
sys.path.insert(0, PARENT_DIR)
sys.path.insert(0, FINAL_DIR)
#pylint: disable=wrong-import-position
from backend import user_input as ui
#pylint: enable=wrong-import-position
#pylint: enable=duplicate-code
# pylint: enable=wrong-import-position

#Constants
YEAR = 365
QUARTER = 90
MONTH = 30
INITIAL_INV_P1 = 10000
INITIAL_INV_P2 = 10000
LARGE_CAP_P1 = 0.4
MED_CAP_P1 = 0.3
SMALL_CAP_P1 = 0.3
LARGE_CAP_P2 = 0.5
BOND_01_P2 = 0.25
BOND_35_P2 = 0.25
START_P1 = pd.Timestamp('2008-01-01 00:00:00')
START_P2 = pd.Timestamp('2010-01-01 00:00:00')
END_P1 = pd.Timestamp('2018-01-01 00:00:00')
END_P2 = pd.Timestamp('2018-01-01 00:00:00')

THRESHOLD_A = 0
THRESHOLD_B = None
RETURN_FREQ_A = 10
RETURN_FREQ_B = 5
START_GRAPH_A = pd.Timestamp('2013-01-01 00:00:00')
START_GRAPH_B = pd.Timestamp('2011-01-01 00:00:00')
END_GRAPH_A = pd.Timestamp('2018-01-01 00:00:00')
END_GRAPH_B = pd.Timestamp('2018-01-01 00:00:00')


TEST_USER_INPUT = [{
    'name': 'Portfolio 1',
    'input': {
        'Initial investment': INITIAL_INV_P1,
        'Investment classes': {
            'U.S. large-cap stocks (Wilshire index)': LARGE_CAP_P1,
            'U.S. mid-cap stocks (Wilshire index)': MED_CAP_P1,
            'U.S. small-cap stocks (Wilshire index)': SMALL_CAP_P1
        },
        'Rebalancing frequency (days)': QUARTER,
        'Start date': START_P1,
        'End date': END_P1
    }
}, {
    'name': 'Portfolio 2',
    'input': {
        'Initial investment': INITIAL_INV_P2,
        'Investment classes': {
            'U.S. large-cap stocks (S&P 500 index)': LARGE_CAP_P2,
            'U.S. Treasury bonds, 0-1 year (S&P index)': BOND_01_P2,
            'U.S. Treasury bonds, 3-5 year (S&P index)': BOND_35_P2
        },
        'Rebalancing frequency (days)': QUARTER,
        'Start date': START_P2,
        'End date': END_P2
    }
}]

TEST_USER_PARAM_A = {
    'Measure of return': 'Change in log of portfolio value',
    'Measure of risk': 'Probability of return below a threshold',
    'Period of return (days) to use for risk measure': YEAR,
    'Threshold rate of return': THRESHOLD_A,
    'Frequency to measure return': RETURN_FREQ_A,
    'Start of period to display': START_GRAPH_A,
    'End of period to display': END_GRAPH_A,
    'Display annualized return': False,
    'Use annualized return for risk measure': False
}

TEST_USER_PARAM_B = {
    'Measure of return': 'Percent change in portfolio value',
    'Measure of risk': 'Standard deviation of return',
    'Period of return (days) to use for risk measure': MONTH,
    'Threshold rate of return': THRESHOLD_B,
    'Frequency to measure return': RETURN_FREQ_B,
    'Start of period to display': START_GRAPH_B,
    'End of period to display': END_GRAPH_B,
    'Display annualized return': True,
    'Use annualized return for risk measure': True
}


class UnitTests(unittest.TestCase):
    '''Set of unittests for the functions and generate_portfolios
     modules.

    Each function in this class is a self contained unittest.
    All queries necessary for execution are run inside the functions
    without using and global results or variables.
    '''

    def test_portfolio_return_type(self):
        '''check if number of records is as expected.
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
        '''
        # file_name = './Data/SP500.csv'
        portfolio_1 = ui.portfolio_from_input(TEST_USER_INPUT[0]['input'])
        self.assertEqual(pd.core.frame.DataFrame, type(portfolio_1))

    def test_portfolio_column_name(self):
        '''check if number of records is as expected.
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
        '''
        portfolio_1 = ui.portfolio_from_input(TEST_USER_INPUT[0]['input'])
        col_name = list(portfolio_1)[0]
        self.assertEqual(col_name, 'Value')

    def test_portfolio_column_num(self):
        '''check if number of records is as expected.
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
        '''
        portfolio_1 = ui.portfolio_from_input(TEST_USER_INPUT[0]['input'])
        col_num = len(list(portfolio_1))
        self.assertEqual(col_num, 1)

    def test_portfolio_row_num(self):
        '''check if number of records is as expected.
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
        '''
        portfolio_1 = ui.portfolio_from_input(TEST_USER_INPUT[0]['input'])
        row_num = len(portfolio_1)
        self.assertGreater(row_num, 0)

    def test_export_return_type(self):
        '''check if number of records is as expected.
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
        '''
        export_data = ui.export_user_portfolios(
            user_portfolio_list=[portfolio['input'] for portfolio in TEST_USER_INPUT],
            user_labels=[portfolio['name'] for portfolio in TEST_USER_INPUT],
            user_parameters=TEST_USER_PARAM_A)
        self.assertEqual(pd.core.frame.DataFrame, type(export_data))

    def test_export_portfolio_col_names(self):
        '''check if number of records is as expected.
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
        '''
        export_data = ui.export_user_portfolios(
            user_portfolio_list=[portfolio['input'] for portfolio in TEST_USER_INPUT],
            user_labels=[portfolio['name'] for portfolio in TEST_USER_INPUT],
            user_parameters=TEST_USER_PARAM_A
        )
        actual_col_names = sorted(list(export_data))
        expected_col_names = ['Label', 'Return', 'Risk']
        self.assertEqual(actual_col_names, expected_col_names)

    def test_export_portfolio_col_num(self):
        '''check if number of records is as expected.
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
        '''
        export_data = ui.export_user_portfolios(
            user_portfolio_list=[portfolio['input'] for portfolio in TEST_USER_INPUT],
            user_labels=[portfolio['name'] for portfolio in TEST_USER_INPUT],
            user_parameters=TEST_USER_PARAM_A
        )
        col_num = len(list(export_data))
        self.assertEqual(col_num, 3)

    def test_export_portfolio_row_num(self):
        '''check if number of records is as expected.
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
        '''
        export_data = ui.export_user_portfolios(
            user_portfolio_list=[portfolio['input'] for portfolio in TEST_USER_INPUT],
            user_labels=[portfolio['name'] for portfolio in TEST_USER_INPUT],
            user_parameters=TEST_USER_PARAM_A
        )
        actual_row_num = len(export_data)
        expected_row_num = len(TEST_USER_INPUT)
        self.assertEqual(actual_row_num, expected_row_num)


SUITE1 = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE1)
