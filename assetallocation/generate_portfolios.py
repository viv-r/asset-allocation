import functions

stock = invest_dataframe('Data/SP500.csv')
bond = invest_dataframe('Data/BAMLCC0A1AAATRIV.csv')

"""Generate portfolios ranging from 10-90% stocks with the remainder in bonds.
4-year time horizon (2014-18), rebalance every 90 days."""

a = date(2014, 1, 2)
b = date(2018, 1, 3)

def gen_allocation(stock, bond, stockshare, start=a, end=b, rebal_time=90):
	assert stockshare >= 0 and stockshare <= 1
	alloc = [(stock, stockshare), (bond, 1 - stockshare)]
	return track_portfolio(alloc, rebal_time, a, b)

s9b1 = gen_allocation(stock, bond, .9)
s8b2 = gen_allocation(stock, bond, .8)
s7b3 = gen_allocation(stock, bond, .7)
s6b4 = gen_allocation(stock, bond, .6)
s5b5 = gen_allocation(stock, bond, .5)
s4b6 = gen_allocation(stock, bond, .4)
s3b7 = gen_allocation(stock, bond, .3)
s2b8 = gen_allocation(stock, bond, .2)
s1b9 = gen_allocation(stock, bond, .1)

labels = [str(x/10.) + " stocks " + str(1 - x/10.) + " bonds"  for x in range(1, 10)]

label_risk_return(labels=[], 
	portfolios=[s9b1, s8b2, s7b3, s6b4, s5b5, s4b6, s3b7, s2b8, s1b9])