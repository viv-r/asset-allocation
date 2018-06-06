# DATA 515 Project - Asset allocation [![Build Status](https://travis-ci.org/viv-r/asset-allocation.svg?branch=master)](https://travis-ci.org/viv-r/asset-allocation) [![Coverage Status](https://coveralls.io/repos/github/viv-r/asset-allocation/badge.svg?branch=master)](https://coveralls.io/github/viv-r/asset-allocation?branch=master)

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

## Project structure
```
.
├── Data
│   ├── AGG.csv
│   ├── BAMLCC0A1AAATRIV.csv
│   ├── BAMLCC0A4BBBTRIV.csv
│   ├── RU2000TR.csv
│   ├── RU3000TR.csv
│   ├── RUMIDCAPTR.csv
│   ├── SP01BOND.csv
│   ├── SP13BOND.csv
│   ├── SP35BOND.csv
│   ├── SP500.csv
│   ├── SP57BOND.csv
│   ├── SPUSBOND.csv
│   ├── WILL5000INDFC.csv
│   ├── WILLLRGCAP.csv
│   ├── WILLMIDCAP.csv
│   ├── WILLSMLCAP.csv
│   ├── ^DJI.csv
│   ├── ^GSPC.csv
│   └── dailypricehistory.xls
├── LICENSE
├── README.md
├── assetallocation
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── demo_portfolios.cpython-36.pyc
│   │   ├── functions.cpython-36.pyc
│   │   ├── generate_portfolios.cpython-36.pyc
│   │   └── user_input.cpython-36.pyc
│   ├── app.py
│   ├── backend
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── demo_portfolios.cpython-36.pyc
│   │   │   ├── functions.cpython-36.pyc
│   │   │   └── user_input.cpython-36.pyc
│   │   ├── demo_portfolios.py
│   │   ├── functions.py
│   │   └── user_input.py
│   ├── frontend
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── callbacks.cpython-36.pyc
│   │   │   ├── datasets.cpython-36.pyc
│   │   │   ├── datasets_tab.cpython-36.pyc
│   │   │   ├── introduction_tab.cpython-36.pyc
│   │   │   ├── page.cpython-36.pyc
│   │   │   ├── portfolios_tab.cpython-36.pyc
│   │   │   ├── risk_return_tab.cpython-36.pyc
│   │   │   ├── riskreturn_graph.cpython-36.pyc
│   │   │   ├── state.cpython-36.pyc
│   │   │   └── timeperiod_input.cpython-36.pyc
│   │   ├── datasets_tab.py
│   │   ├── introduction_tab.py
│   │   ├── page.py
│   │   ├── portfolios_tab.py
│   │   └── risk_return_tab.py
│   └── tests
│       └── __pycache__
│           ├── __init__.cpython-36.pyc
│           ├── functions_test.cpython-36-PYTEST.pyc
│           ├── test_core.cpython-36-PYTEST.pyc
│           └── test_core.cpython-36.pyc
├── doc
│   ├── Benchmark\ stock\ indices.docx
│   ├── Design.md
│   ├── Technology\ Review\ Presentation.pdf
│   ├── backend.png
│   ├── components_diagram.jpg
│   └── frontend.png
├── examples
│   ├── demo_script.py
│   ├── examples.md
│   ├── tab-1-introduction.png
│   ├── tab-2-portfolios.png
│   ├── tab-3-risk-return-graph.png
│   └── tab-4-datasets.png
├── htmlcov
│   ├── assetallocation_tests_functions_test_py.html
│   ├── coverage_html.js
│   ├── index.html
│   ├── jquery.ba-throttle-debounce.min.js
│   ├── jquery.hotkeys.js
│   ├── jquery.isonscreen.js
│   ├── jquery.min.js
│   ├── jquery.tablesorter.min.js
│   ├── keybd_closed.png
│   ├── keybd_open.png
│   ├── status.json
│   └── style.css
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── functions_test.cpython-36-PYTEST.pyc
    │   └── test_user_input.cpython-36-PYTEST.pyc
    ├── functions_test.py
    ├── test_frontend.py
    └── test_user_input.py
```

## Team members

- Vamsy Alturi
- Will Bishop
- Vivek Pagadala
