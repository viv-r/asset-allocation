# Data515 Project - Asset allocation [![Build Status](https://travis-ci.org/viv-r/asset-allocation.svg?branch=master)](https://travis-ci.org/viv-r/asset-allocation) [![Coverage Status](https://coveralls.io/repos/github/viv-r/asset-allocation/badge.svg?branch=master)](https://coveralls.io/github/viv-r/asset-allocation?branch=master)

## Background

  - Predicting returns on investment portfolios is uncertain
  - Investors want to understand risk-reward tradeoff
  - Different quantitative measures of risk and return may yield different investment decisions
  
## Goal

  - Help investors understand how the numbers that drive their decisions are sensitive to their measures of risk and return and assumptions about how the past predicts the future

## Data used

  - U.S. stock market indices
    - S&P 500 index
    - Wilshire large, medium, and small capitalization indices
  - U.S. Treasury bond market indices (S&P)
    - 0-1 year maturity
    - 1-3 year
    - 3-5 year
    - 5-7 year
  - U.S. corporate investment-grade bonds
    - Bloomberg Barclays AAA index
    - Bloomberg Barclays BBB index

## Use cases

Our app allows a user to:
  - Compare asset portfolios composed of different types of stocks and bonds
  - Compare quantitative measures of risk
    - Standard deviation of return, historical probability of loss
  - View risk and return over different time horizons
  - See how well past risk and return predict the future
