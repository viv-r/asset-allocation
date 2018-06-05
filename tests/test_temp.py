import sys
import os
import inspect
import unittest
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
GPARENT_DIR = os.path.dirname(PARENT_DIR)

sys.path.insert(0, GPARENT_DIR)

from assetallocation import functions

FILE_NAME = "./Data/SP500.csv"

data = functions.invest_dataframe(FILE_NAME)

# print(data)

start = pd.Timestamp('1986-01-02 00:00:00', tz=None)
end = pd.Timestamp('2018-01-03 00:00:00', tz=None)

r = functions.calc_risk(data,start,end,risk_type="proba",return_type='log')

print(r)
# # pd.datetime(1975-01-01)
# # startval = float(data.loc[start][0])
# # endval = float(data.loc[end][0])

# # print(startval,endval)
# # o = functions.calc_return(data,start,end,return_type='log',annualize=True)
# # print(type(o))

# o2 = functions.return_list(data,start,end)
# print(type(o2))
# print(o2.shape)

# num_days = end-start
# days = str(num_days)
# print(days[:days.find(" ")])
# print(o)
# FILE_NAME_1 = "./Data/SP35BOND.csv"

# a = functions.invest_dataframe(FILE_NAME)
# print(a)

# # a_1 = functions.invest_dataframe(FILE_NAME_1)
# c1 = "/"
# c2 = "."
# break1 = [pos for pos, char in enumerate(FILE_NAME) if char == c1]
# break2 = [pos for pos, char in enumerate(FILE_NAME) if char == c2]
# print(FILE_NAME[break1[-1]+1:break2[-1]])
# print(list(a)[0])
# # print(list(a_1))


# print(a.shape)
# print(a_1.shape)

# def file_len(fname):
    # with open(fname) as f:
    #     for i, l in enumerate(f):
    #         pass
    # return i + 1

# len1 = file_len(FILE_NAME)
# len2 = file_len(FILE_NAME_1)

# print(len1)
# print(len2)

# print(len1 - a.shape[0])
# print(len2 - a_1.shape[0])