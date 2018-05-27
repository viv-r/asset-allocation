"""Tests user_input.py module"""

import numpy as np
import pandas as pd
import user_input as ui

test_user_input_1 = {
	'Initial investment': 10000,
	'Investment classes': {
		'U.S. large-cap stocks (S&P 500 index)': 0.4,
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
		'U.S. corporate bonds (investment-grade)': 0.5
		},
	'Rebalancing frequency (days)': 90,
	'Start date': pd.Timestamp('2014-01-01 00:00:00'),
	'End date': pd.Timestamp('2018-01-01 00:00:00')
}

test_user_param = {
	'Measure of return': 'Change in log of portfolio value',
	'Measure of risk': 'Probability of return below a threshold',
	'Period of return to measure': 'Annual',
	'Threshold rate of return': 0.0,
	'Frequency to measure return': 10,
	'Start of period to display': pd.Timestamp('2014-01-01 00:00:00'),
	'End of period to display': pd.Timestamp('2018-01-01 00:00:00')
}

portfolio_1 = ui.portfolio_from_input(test_user_input_1)
portfolio_2 = ui.portfolio_from_input(test_user_input_2)
export_data = ui.export_user_portfolios(
	user_portfolio_list=[test_user_input_1, test_user_input_2],
	user_labels=['Portfolio 1', 'Portfolio 2'],
	user_parameters=test_user_param
	)