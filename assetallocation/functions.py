import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from datetime import date, timedelta

# Basic functions for asset allocation tool


def invest_dataframe(filename, sep=','):
    """
    Loads a data set containing an investment (stock or bond index).
    Checks that the data set has two columns: a date and an index value.
    Creates a DateTimeIndex.
    Checks there is only one value per date.
    INPUT: filename = name of CSV file, sep = separator in CSV file
    """
    data = pd.read_csv(filename, sep=sep, index_col=0,
                       parse_dates=[0], infer_datetime_format=True)
    # Get rid of missing and non-numeric values
    data = data.apply(pd.to_numeric, errors='coerce').dropna()
    assert data.shape[1] == 1
    assert type(data.index) == pd.core.indexes.datetimes.DatetimeIndex
    assert data.index.nunique() == len(data)
    # Fill missing dates with most recent value
    # Source: https://stackoverflow.com/questions/19324453/add-missing-dates-to-pandas-dataframe
    start, end = min(data.index), max(data.index)
    idx = pd.date_range(start, end)
    data = data.reindex(idx)
    data.fillna(method='ffill', axis=0, inplace=True)

    return data


def calc_return(data, start, end, return_type='percent', annualize=False):
    """
    Calculates rate of return on a data set between two dates.
    Allows for either percentage rate or log growth.
    INPUTS: start, end = datetimes; data = data frame of investment values
    Annualize = whether to return annualized return instead of total return
    """
    startval = float(data.loc[start][0])
    endval = float(data.loc[end][0])
    # Divisor = number of years if annualized return, else 1
    if annualize:
        div = (end - start) / timedelta(days=365.2425)
    else:
        div = 1
    # Calculate percentage or log return
    if return_type == 'percent':
        total = endval / startval
        return total**(1 / div) - 1
    elif return_type == 'log':
        total = np.log(endval) - np.log(startval)
        return total / div
    else:
        raise Exception("Return type must be percent or log.")


# We will want to cache this
def return_list(data, start, end, period=365, freq=1, return_type='percent'):
    """
    Calculates a list of rates of return over a range of time.
    INPUTS:
    start = overall start date, end = overall end date
    period = # of days over which to calculate the rate of return
        Example: yearly return = 365
    freq = how often to sample
        Example: calculate return every day = 1, once a year = 365
    return_type = measure of return (percent or log)
    Ignores partial periods at the end when freq > 1 day.
    """
    # Use date_range
    return np.array([calc_return(data, day, day + timedelta(days=period), return_type=return_type)
                     for day in pd.date_range(start, end - timedelta(days=period),
                                              freq=timedelta(days=freq))])


def calc_risk(data, start, end, risk_type='stddev', period=365,
    freq=1, threshold=0, return_type='percent', annualize=False):
    """
    Risk measure:
    - proba = historical probability of return below a certain value
    - stddev = standard deviation of rate of return
    INPUTS:
    period = # of days over which to calculate rate of return
        Example: yearly return = 365
    freq = how often to sample
        Example: calculate return every day = 1, once a year = 365
    rate = threshold rate of return
    return_type = measure of return (percent or log)
    annualize = whether to use annualized return
    """
    if risk_type == 'stddev':
        return np.std(return_list(data, start, end, period=period, freq=freq,
                                  return_type=return_type, annualize=annualize))
    elif risk_type == 'proba':
        return np.mean(return_list(data, start, end, period=period, freq=freq, 
                                   return_type=return_type, annualize=annualize) < threshold)
    else:
        raise Exception('Risk measure must be sttdev or proba.')


# Track portfolio with rebalancing

def track_portfolio(initial, percent, rebal_time, start, end):
    """
    Computes values of a portfolio with given percentages of certain indices.
    INPUTS:
    initial = amount invested on starting day
    percent = list of tuples of investment data frames with percentages
        (must add to 1)
    rebal_time = how often to rebalance the portfolio (measured in days)
    start, end = start and end dates to compute values
    """
    assert np.isclose(sum(p[1] for p in percent), 1)
    #assert len(percent) == len(set(p[0] for p in percent))
    portfolio = pd.Series()
    portfolio[start] = initial
    for rebal_day in pd.date_range(start, end, freq=timedelta(days=rebal_time)):
        value = portfolio[rebal_day]
        shares = [(k, value * p / (k.loc[rebal_day][0])) for k, p in percent]
        portfolio = pd.concat([portfolio, share_growth(shares, rebal_day + timedelta(days=1),
                                                       min(end, rebal_day + timedelta(days=rebal_time)))])
    return pd.DataFrame(portfolio, columns=['Value'])

#Track portfolio with rebalancing and cacheing - needs fix to unhashable types problem
# portfolio_cache = {}

# def index_to_portfolio(initial, portfolio_index, start, end):
#     portfolio = pd.DataFrame(initial / portfolio_index.loc[start] * portfolio_index.loc[start:end+1], columns=['Value'])
#     return portfolio

# def track_portfolio_cache(initial, percent, rebal_time, start, end):
#     """
#     Computes values of a portfolio with given percentages of certain indices.
#     INPUTS:
#     initial = amount invested on starting day
#     percent = list of tuples of investment data frames with percentages
#         (must add to 1)
#     rebal_time = how often to rebalance the portfolio (measured in days)
#     start, end = start and end dates to compute values
#     CACHE:
#     Contains index for each (percent, rebal) pair - no need for separate initial investments
#     """
#     if (percent, rebal) in portfolio_cache:
#         portfolio_index = portfolio_cache[(percent, rebal)]
#     else:
#         assert np.isclose(sum(p[1] for p in percent), 1)
#         #assert len(percent) == len(set(p[0] for p in percent))
#         #If not in cache, create a new index, then multiply by initial value
#         #NOTE: This does not allow flexibility in the start date for rebalancing counter...
#         portfolio_index = pd.Series()
#         index_start = max([min(data.index) for data, pct in percent])
#         index_end = min([max(data.index) for data, pct in percent])
#         portfolio_index[index_start] = 100
#         for rebal_day in pd.date_range(index_start, index_end, freq=timedelta(days=rebal_time)):
#             value = portfolio_index[rebal_day]
#             shares = [(k, value * p / (k.loc[rebal_day][0])) for k, p in percent]
#             portfolio_index = pd.concat([portfolio_index,
#                                          share_growth(shares, rebal_day + timedelta(days=1),
#                                                       min(end, rebal_day + timedelta(days=rebal_time)))])
#         portfolio_cache[(percent, rebal)] = portfolio_index
#     return index_to_portfolio(initial, portfolio_index, start, end)


# Track portfolio for unchanging number of shares, no rebalancing
def share_growth(shares, start, end):
    """
    Computes growth of a portfolio with a given number of shares of different indices.
    INPUTS:
    shares = list of tuples of investment data frames with number of shares
    start, end = start and end dates to compute values
    """
    return sum(s * k.loc[start:end].iloc[:, 0] for k, s in shares)


def get_risk_return(portfolios, start, end, return_type='percent', annualize_return=False, 
    risk_type='stddev', annualize_risk=False, period=365, freq=None, threshold=None):
    """
    INPUTS:
    portfolios = list of portfolio data frames
    start, end = start and end dates for measuring risk and return
    period = period for measuring risk
    freq = how often to sample for measuring risk
    rate = threshold rate of return (for probability risk measure)
    return_type = percent or log
    risk_type = stddev or proba
    annualize_return = whether to display annualized return (y axis)
    annualize_risk = whether to use annualized return for measuring risk (x axis)
    """
    y = [calc_return(p, start, end, return_type=return_type, annualize=annualize_return) for p in portfolios]
    x = [calc_risk(p, start, end, threshold=threshold, period=period, freq=freq, 
                   risk_type=risk_type, return_type=return_type, annualize=annualize_risk)
            for p in portfolios]
    return pd.DataFrame({'Risk': x, 'Return': y})


def label_risk_return(labels, portfolios, start, end, return_type='percent', annualize_return=False, 
    risk_type='stddev', annualize_risk=False, period=365, freq=None, threshold=None):
    """
    INPUTS:
    labels = how we want the portfolios described/labeled in the graph
    others = see get_risk_return
    """
    df = get_risk_return(portfolios, start, end, return_type=return_type, annualize_return=annualize_return,
                         risk_type=risk_type, annualize_risk=annualize_risk, period=period, freq=freq, threshold=threshold)
    assert len(labels) == len(df)
    df['Label'] = labels
    return df


# def plot_risk_return(portfolios, start, end, return_type='percent', risk_type='stddev', period=365, freq=None, rate=None):
#     """
#     INPUTS:
#     see get_risk_return
#     """
#     df = get_risk_return(portfolios, start, end, return_type='percent',
#                          risk_type='stddev', period=365, freq=None, rate=None)
#     plt.scatter(['Risk', 'Return'], data=df)
#     plt.xlabel("Total %s return over given time period") % (return_type)
#     plt.ylabel("Risk over given time period")
#     plt.show()
