"""Functions to translate user input into portfolio"""

import numpy as np
import pandas as pd
from functions import *


#Dictionary translating descriptions of investment classes to data sets
investment_class_dict = {
    'U.S. large-cap stocks (S&P 500 index)': invest_dataframe('../Data/SP500.csv'),
    'U.S. large-cap stocks (Wilshire index)': invest_dataframe('../Data/WILLLRGCAP.csv'),
    'U.S. mid-cap stocks (Wilshire index)': invest_dataframe('../Data/WILLMIDCAP.csv'),
    'U.S. small-cap stocks (Wilshire index)': invest_dataframe('../Data/WILLSMLCAP.csv'),
    'U.S. corporate bonds (investment-grade)': invest_dataframe('../Data/BAMLCC0A1AAATRIV.csv'),
    'U.S. Treasury bonds, total market (S&P index)': invest_dataframe('../Data/SPUSBOND.csv'),
    'U.S. Treasury bonds, 0-1 year (S&P index)': invest_dataframe('../Data/SP01BOND.csv'),
    'U.S. Treasury bonds, 1-3 year (S&P index)': invest_dataframe('../Data/SP13BOND.csv'),
    'U.S. Treasury bonds, 3-5 year (S&P index)': invest_dataframe('../Data/SP35BOND.csv'),
    'U.S. Treasury bonds, 5-7 year (S&P index)': invest_dataframe('../Data/SP57BOND.csv'),
    'U.S. Treasury bonds, long-term': None, #fill in
    'U.S. municipal tax-exempt bonds': None, #fill in
    'International growth stocks': None, #fill in
    'International value stocks': None, #fill in
    'Cash at inflation': None #fill in inflation data set
    #Expand as necessary, possibly including individual stock and bond data sets
}


def portfolio_from_input(user_input):
    """INPUTS:
    user_input: dictionary of user inputs for a single portfolio including:
    - Initial investment
    - Investment classes
        - Percentages of different investment classes
    - Rebalancing frequency (days)
    - Start date
    - End date
    OUTPUT: data for tracking portfolio 
    """
    initial = user_input['Initial investment']
    rebal_time = user_input['Rebalancing frequency (days)']
    start = user_input['Start date']
    end = user_input['End date']
    percent_tuple = [(investment_class_dict[invest_class], pct)
        for invest_class, pct in user_input['Investment classes'].items()
    ]
    return track_portfolio(initial, percent_tuple, rebal_time, start, end)


return_type_dict = {
    'Percent change in portfolio value': 'percent',
    'Change in log of portfolio value': 'log'
}

risk_type_dict = {
    'Standard deviation of return': 'stddev',
    'Probability of return below a threshold': 'proba'
}

return_period_dict = {
    'Annual': 365,
    '90-day': 90,
    '30-day': 30,
    'Daily': 1
}


def export_user_portfolios(user_portfolio_list, user_labels, user_parameters):
    """INPUTS:
    user_portfolio_list: portfolios user has built
    user_labels: user-defined (or auto-generated?) labels for each portfolio
    return_type: user's preferred return measure (percent or log)
    risk_type: user's preferred risk measure
    period = period for measuring risk
    freq = how often to sample for measuring risk
    rate = threshold rate of return (for probability risk measure)
    start = start date for graphing
    end = end date for graphing
    OUTPUT: data for graphing risk and return of user's chosen portfolios
    """
    portfolio_list = [portfolio_from_input(user_input) for user_input in user_portfolio_list]
    return_type = return_type_dict[
        user_parameters['Measure of return']
        ]
    risk_type = risk_type_dict[
        user_parameters['Measure of risk']
        ]
    period = return_period_dict[
        user_parameters['Period of return to measure']
        ]
    start = user_parameters['Start of period to display']
    end = user_parameters['End of period to display']
    freq = user_parameters['Frequency to measure return'] #can be None; not sure if this should be a user input
    rate = user_parameters['Threshold rate of return'] #can be None
    return label_risk_return(user_labels, portfolio_list, start, end,
        return_type, risk_type, period, freq, rate)