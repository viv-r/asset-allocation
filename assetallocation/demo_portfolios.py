"""Creates many portfolios for in-class demonstration"""

import numpy as np
import pandas as pd
import user_input as ui

def demo_portfolios(initial, rebal_time, start, end, user_parameters,
    stock_only=True, bond_only=True, mix=True):

    #Large-medium-small capitalization U.S. stock splits

    splits = {}
    if stock_only:
        for x in range(11):
            for y in range(11 - x):
                z = 10 - x - y
                label = "Stock LMS %d-%d-%d" %(x, y, z)
                splits[label] = \
                    {'U.S. large-cap stocks (Wilshire index)': x/10.,
                    'U.S. mid-cap stocks (Wilshire index)': y/10.,
                    'U.S. small-cap stocks (Wilshire index)': z/10.}

    #Short and medium term U.S. Treasury bond splits

    if bond_only:
        for t in range(0, 11, 2):
            for u in range(0, 11-t, 2):
                for v in range(0, 11-t-u, 2):
                    w = 10 - t - u - v
                    label = "Bond split %d-%d-%d-%d" %(t, u, v, w)
                    splits[label] = \
                        {
                        'U.S. Treasury bonds, 0-1 year (S&P index)': w/10.,
                        'U.S. Treasury bonds, 1-3 year (S&P index)': v/10.,
                        'U.S. Treasury bonds, 3-5 year (S&P index)': u/10.,
                        'U.S. Treasury bonds, 5-7 year (S&P index)': t/10.
                        }

    #Stock (3-tier) and total bond market mixed portfolios

    if mix:
        for p in range(11):
            for q in range(11-p):
                for r in range(11-p-q):
                    s = 10 - p - q - r
                    label = "Stock LMS - Total bond %d-%d-%d-%d" %(p, q, r, s)
                    splits[label] = \
                        {
                        'U.S. large-cap stocks (S&P 500 index)': p/10.,
                        'U.S. mid-cap stocks (Wilshire index)': q/10.,
                        'U.S. small-cap stocks (Wilshire index)': r/10.,
                        'U.S. Treasury bonds, total market (S&P index)': s/10.
                        }

    portfolios = {label:
        {'Initial investment': initial,
        'Investment classes': ivc,
        'Rebalancing frequency (days)': rebal_time,
        'Start date': start,
        'End date': end}
        for label, ivc in splits.items()}
    #Needs refactoring - not efficient
    user_portfolio_list = portfolios.values()
    user_labels = portfolios.keys()
    return ui.export_user_portfolios(user_portfolio_list, user_labels, user_parameters)

test_user_param_A = {
    'Measure of return': 'Change in log of portfolio value',
    'Measure of risk': 'Probability of return below a threshold',
    'Period of return (days) to use for risk measure': 365,
    'Threshold rate of return': 0.0,
    'Frequency to measure return': 10,
    'Start of period to display': pd.Timestamp('2009-01-01 00:00:00'),
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
    'Start of period to display': pd.Timestamp('2009-01-01 00:00:00'),
    'End of period to display': pd.Timestamp('2018-01-01 00:00:00'),
    'Display annualized return': True,
    'Use annualized return for risk measure': True
}

start = pd.Timestamp('2009-01-01 00:00:00')
end = pd.Timestamp('2018-01-01 00:00:00')
test_demo_portfolios_A = demo_portfolios(10000, 90, start, end, test_user_param_A)
test_demo_portfolios_B = demo_portfolios(10000, 90, start, end, test_user_param_B)