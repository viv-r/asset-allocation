from datetime import date, timedelta
import pandas as pd
from assetallocation import functions


# store calls to get_graph_data
cache = {}

def get_graph_data(from_year=2014, to_year=2018):
    if (from_year, to_year) in cache:
        return cache[(from_year, to_year)]

    """Generate portfolios ranging from 10-90% stocks with the remainder in bonds.
    4-year time horizon (2014-18), rebalance every 90 days."""

    stock = functions.invest_dataframe('./Data/SP500.csv')
    bond = functions.invest_dataframe('./Data/BAMLCC0A1AAATRIV.csv')

    a = pd.Timestamp(str(from_year) + '-01-02 00:00:00', tz=None)
    b = pd.Timestamp(str(to_year) + '-01-03 00:00:00', tz=None)
    print(from_year, to_year)

    def gen_allocation(stock, bond, stockshare, start=a, end=b, rebal_time=90):
        assert stockshare >= 0 and stockshare <= 1
        alloc = [(stock, stockshare), (bond, 1 - stockshare)]
        return functions.track_portfolio(10000, alloc, rebal_time, a, b)

    portfolios = [gen_allocation(stock, bond, i / 10) for i in range(1, 10)]

    labels = [str(100 - x) + "% stocks " + str(x) +
              "% bonds" for x in range(10, 100, 10)]

    data = functions.label_risk_return(labels=labels, portfolios=portfolios, start=a, end=b)

    res = (data.Return.values, data.Risk.values, data.Label.values)
    cache[(from_year, to_year)] = res
    return res
