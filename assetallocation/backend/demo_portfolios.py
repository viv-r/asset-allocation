"""
This file creates many examples of portfolios for the in-class demonstration.
"""
import pandas as pd


#Constants
YEAR = 365
QUARTER = 90
MONTH = 30

THRESHOLD_A = 0
THRESHOLD_B = None
RETURN_FREQ_A = 10
RETURN_FREQ_B = 5
START_GRAPH_A = pd.Timestamp('2009-01-01 00:00:00')
START_GRAPH_B = pd.Timestamp('2009-01-01 00:00:00')
END_GRAPH_A = pd.Timestamp('2018-01-01 00:00:00')
END_GRAPH_B = pd.Timestamp('2018-01-01 00:00:00')


def demo_portfolios(initial, rebal_time, start, end, _user_parameters,
                    stock_only=True, bond_only=False, mix=False):
    """
    Creates a list of demo portfolios, each containing a list of assets
    with varying weights.

    Args:
        initial: amount invested on first day
        rebal_time: portfolio rebalancing frequency (in days)
        start, end: start and end dates
        stock_only: whether to use stock-only portfolios
        bond_only: whether to use bond-only portfolios
        mix: whether to use stock-bond mix portfolios
    Returns:
        A list of portfolios
    """
    # pylint: disable=invalid-name, too-many-locals, redefined-outer-name
    # Disabling a pylint errors since this function is readable
    # with the single loop variable names (invalid-name) and all of them
    # are required (too-many-locals error)

    # Large-medium-small capitalization U.S. stock splits

    splits = {}
    if stock_only:
        for x in range(0, 11, 2):
            for y in range(0, 11 - x, 2):
                z = 10 - x - y
                label = "Stock LMS %d-%d-%d" % (x, y, z)
                splits[label] = {
                    'U.S. large-cap stocks (Wilshire index)': x / 10.,
                    'U.S. mid-cap stocks (Wilshire index)': y / 10.,
                    'U.S. small-cap stocks (Wilshire index)': z / 10.
                }

    # Short and medium term U.S. Treasury bond splits

    if bond_only:
        for t in range(0, 11, 2):
            for u in range(0, 11 - t, 2):
                for v in range(0, 11 - t - u, 2):
                    w = 10 - t - u - v
                    label = "Bond split %d-%d-%d-%d" % (t, u, v, w)
                    splits[label] = {
                        'U.S. Treasury bonds, 0-1 year (S&P index)': w / 10.,
                        'U.S. Treasury bonds, 1-3 year (S&P index)': v / 10.,
                        'U.S. Treasury bonds, 3-5 year (S&P index)': u / 10.,
                        'U.S. Treasury bonds, 5-7 year (S&P index)': t / 10.
                    }

    # Stock (3-tier) and total bond market mixed portfolios

    if mix:
        for p in range(0, 11, 2):
            for q in range(0, 11 - p, 2):
                for r in range(0, 11 - p - q, 2):
                    s = 10 - p - q - r
                    label = "Stock LMS - Total bond %d-%d-%d-%d" % (p, q, r, s)
                    splits[label] = {
                        'U.S. large-cap stocks (S&P 500 index)': p / 10.,
                        'U.S. mid-cap stocks (Wilshire index)': q / 10.,
                        'U.S. small-cap stocks (Wilshire index)': r / 10.,
                        'U.S. Treasury bonds, total market (S&P index)': s / 10.
                    }

    portfolios = [{
        'name': label,
        'id': label,
        'input': {
            'Initial investment': initial,
            'Investment classes': ivc,
            'Rebalancing frequency (days)': rebal_time,
            'Start date': start,
            'End date': end
        }
    } for label, ivc in splits.items()]

    return portfolios


#Test sets of user parameters for graphing
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

START_PORTFOLIOS = pd.Timestamp('2009-01-01 00:00:00')
END_PORTFOLIOS = pd.Timestamp('2018-01-01 00:00:00')
TEST_DEMO_PORTFOLIOS_A = demo_portfolios(10000, 90, START_PORTFOLIOS,
                                         END_PORTFOLIOS, TEST_USER_PARAM_A)
TEST_DEMO_PORTFOLIOS_B = demo_portfolios(10000, 90, START_PORTFOLIOS,
                                         END_PORTFOLIOS, TEST_USER_PARAM_B)
