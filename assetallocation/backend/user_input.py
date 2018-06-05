"""
This file contains the functions which take the user inputs
from the frontend, send them to the backend to interact with
the data, then returns the information to the frontend for graphing.
"""
from backend.functions import invest_dataframe, track_portfolio_cache, label_risk_return

# Dictionary translating descriptions of investment classes to data sets
# Expand as necessary in the future.
INVESTMENT_CLASS_DICT = {
    'U.S. large-cap stocks (S&P 500 index)': invest_dataframe('./Data/SP500.csv'),
    'U.S. large-cap stocks (Wilshire index)': invest_dataframe('./Data/WILLLRGCAP.csv'),
    'U.S. mid-cap stocks (Wilshire index)': invest_dataframe('./Data/WILLMIDCAP.csv'),
    'U.S. small-cap stocks (Wilshire index)': invest_dataframe('./Data/WILLSMLCAP.csv'),
    'U.S. corporate bonds (investment-grade, AAA rated)':
        invest_dataframe('./Data/BAMLCC0A1AAATRIV.csv'),
    'U.S. corporate bonds (investment-grade, BBB rated)':
        invest_dataframe('./Data/BAMLCC0A4BBBTRIV.csv'),
    'U.S. Treasury bonds, total market (S&P index)': invest_dataframe('./Data/SPUSBOND.csv'),
    'U.S. Treasury bonds, 0-1 year (S&P index)': invest_dataframe('./Data/SP01BOND.csv'),
    'U.S. Treasury bonds, 1-3 year (S&P index)': invest_dataframe('./Data/SP13BOND.csv'),
    'U.S. Treasury bonds, 3-5 year (S&P index)': invest_dataframe('./Data/SP35BOND.csv'),
    'U.S. Treasury bonds, 5-7 year (S&P index)': invest_dataframe('./Data/SP57BOND.csv'),
    'U.S. Treasury bonds, long-term': None,  # fill in
    'U.S. municipal tax-exempt bonds': None,  # fill in
    'International growth stocks': None,  # fill in
    'International value stocks': None,  # fill in
    'Cash at inflation': None  # fill in
}


def portfolio_from_input(user_input):
    """
    Translates user input (frontend) to portfolio data (backend).

    Args:
        user_input: dictionary of user inputs for a single portfolio including:
        - Initial investment
        - Investment classes
            - Percentages of different investment classes
        - Rebalancing frequency (days)
        - Start date
        - End date
    Returns:
        Dataframe of values of asset portfolio by date.
    """
    initial = user_input['Initial investment']
    rebal_time = user_input['Rebalancing frequency (days)']
    start = user_input['Start date']
    end = user_input['End date']
    # Every investment class should be different
    assert len(set(user_input['Investment classes'].keys())) == \
        len(user_input['Investment classes'].keys())
    percent_list = [(invest_class, pct)
                    for invest_class, pct in user_input['Investment classes'].items()]
    percent_tuple = tuple(percent_list)
    return track_portfolio_cache(initial, percent_tuple, rebal_time,
                                 start, end, INVESTMENT_CLASS_DICT)


RETURN_TYPE_DICT = {
    'Percent change in portfolio value': 'percent',
    'Change in log of portfolio value': 'log'
}

RISK_TYPE_DICT = {
    'Standard deviation of return': 'stddev',
    'Probability of return below a threshold': 'proba'
}


def export_user_portfolios(user_portfolio_list, user_labels, user_parameters):
    """
    Translates a list of user portfolios to a dataframe ready for export to graph.

    Args:
        user_portfolio_list: portfolios user has built
        user_labels: user-defined (or auto-generated) labels for each portfolio
        user_parameters: user specifications for graphing data, including:
            return_type: user's preferred return measure (percent or log)
            risk_type: user's preferred risk measure
            annualize_return = whether to display annualized return on y axis
            annualize_risk = whether to use annualized return for risk calculation on x axis
            period = period for measuring risk
            freq = how often to sample for measuring risk
            rate = threshold rate of return (for probability risk measure)
            start = start date for graphing
            end = end date for graphing
    Returns:
        Dataframe with labels for graphing risk and return of user's chosen portfolios
    """
    portfolio_list = [portfolio_from_input(user_input) for user_input in user_portfolio_list]
    return_type = RETURN_TYPE_DICT[
        user_parameters['Measure of return']
    ]
    risk_type = RISK_TYPE_DICT[
        user_parameters['Measure of risk']
    ]
    period = user_parameters['Period of return (days) to use for risk measure']
    start = user_parameters['Start of period to display']
    end = user_parameters['End of period to display']
    freq = user_parameters['Frequency to measure return']  # Not sure if this should be a user input
    threshold = user_parameters['Threshold rate of return']  # can be None if risk_type=stddev
    annualize_return = user_parameters['Display annualized return']
    annualize_risk = user_parameters['Use annualized return for risk measure']
    assert isinstance(period, (float, int))
    return label_risk_return(labels=user_labels, portfolios=portfolio_list,
                             start=start, end=end,
                             return_type=return_type, annualize_return=annualize_return,
                             risk_type=risk_type, annualize_risk=annualize_risk,
                             period=period, freq=freq, threshold=threshold)
