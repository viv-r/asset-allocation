"""Tests user_input.py module"""

import numpy as np
import pandas as pd
import user_input as ui

test_user_input_1 = {
    'Initial investment': 10000,
    'Investment classes': {
        'U.S. large-cap stocks (Wilshire index)': 0.4,
        'U.S. mid-cap stocks (Wilshire index)': 0.3,
        'U.S. small-cap stocks (Wilshire index)': 0.3
        },
    'Rebalancing frequency (days)': 90,
    'Start date': pd.Timestamp('2008-01-01 00:00:00'),
    'End date': pd.Timestamp('2018-01-01 00:00:00')
}

test_user_input_2 = {
    'Initial investment': 10000,
    'Investment classes': {
        'U.S. large-cap stocks (S&P 500 index)': 0.5,
        'U.S. Treasury bonds, 0-1 year (S&P index)': 0.25,
        'U.S. Treasury bonds, 3-5 year (S&P index)': 0.25
        },
    'Rebalancing frequency (days)': 90,
    'Start date': pd.Timestamp('2010-01-01 00:00:00'),
    'End date': pd.Timestamp('2018-01-01 00:00:00')
}

test_user_param_A = {
    'Measure of return': 'Change in log of portfolio value',
    'Measure of risk': 'Probability of return below a threshold',
    'Period of return (days) to use for risk measure': 365,
    'Threshold rate of return': 0.0,
    'Frequency to measure return': 10,
    'Start of period to display': pd.Timestamp('2013-01-01 00:00:00'),
    'End of period to display': pd.Timestamp('2018-01-01 00:00:00'),
    'Display annualized return': False,
    'Use annualized return for risk measure': False
}

test_user_param_B = {
    'Measure of return': 'Percent change in portfolio value',
    'Measure of risk': 'Standard deviation of return',
    'Period of return (days) to use for risk measure': 30,
    'Threshold rate of return': None,
    'Frequency to measure return': 5,
    'Start of period to display': pd.Timestamp('2011-01-01 00:00:00'),
    'End of period to display': pd.Timestamp('2018-01-01 00:00:00'),
    'Display annualized return': True,
    'Use annualized return for risk measure': True
}

portfolio_1 = ui.portfolio_from_input(test_user_input_1)
portfolio_2 = ui.portfolio_from_input(test_user_input_2)
export_data_A = ui.export_user_portfolios(
    user_portfolio_list=[test_user_input_1, test_user_input_2],
    user_labels=['Portfolio 1', 'Portfolio 2'],
    user_parameters=test_user_param_A
    )
export_data_B = ui.export_user_portfolios(
    user_portfolio_list=[test_user_input_1, test_user_input_2],
    user_labels=['Portfolio 1', 'Portfolio 2'],
    user_parameters=test_user_param_B
    )