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
FILE_NAME_1 = "./Data/SP35BOND.csv"

a = functions.invest_dataframe(FILE_NAME)
# a_1 = functions.invest_dataframe(FILE_NAME_1)
c1 = "/"
c2 = "."
break1 = [pos for pos, char in enumerate(FILE_NAME) if char == c1]
break2 = [pos for pos, char in enumerate(FILE_NAME) if char == c2]
print(FILE_NAME[break1[-1]+1:break2[-1]])
print(list(a)[0])
# print(list(a_1))


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