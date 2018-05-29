import pandas as pd

portfolios = [{
    'name': 'P1',
    'custom': False,
    'input': {
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
}, {
    'name': 'P2',
    'custom': True,
    'input': {
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
}]

options = {
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
