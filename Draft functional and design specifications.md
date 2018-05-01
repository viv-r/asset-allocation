# COMPONENTS

## Database containing data of stock, bonds, inflation and other market data sources.
## Frontend components:
    ### Inputs:
        - Risk measure selection.
        - Asset alloction model selection (list of portfolios)
        - Time period selection.
    ### Graphs
        - Plot of risk vs reward.
## Backend components:
   ### Data loader:
     - Description:
       - Opens a connection to the database.
       - Constructs a query to fetch the required data.
     - Inputs: Fields to fetch from the data (time period, stock/bond name, etc.)
     - Outputs: Rows from the DB
   ### A function to plot Risk/Reward graph:
     - Description:
        - Call the data loader component.
        - Calculates the output.
     - Inputs: the user selection from the frontend
     - Call the data loader component.

## 1. Risk-reward tradeoff analysis

Compare levels of risk and reward in different portfolios. Allow user to select various time horizons and measures of risk.

### 1a. Measures of risk

Built-in calculator for different methods of measuring risk and volatility in a stock portfolio
- Difference between risk and volatility

## 2. Probabilistic model of future performance based on past

Time-series / probabilistic model. Say you want to invest for a 20-year timeline. How well do past return and risk measures predict the next 20 years of returns?

Investment companies always tell us "past performance is no guarantee of future results". Can we quantify how uncertain it is?

# FUNCTIONS / USE CASES

## 0. Allows the user to see the risk vs reward values for a combination of risk measure, allocation strategy and time period

## 1. Deciding on acceptable level of risk for a given measure

## 2. Seeing how choice of risk measure affects asset allocation decisions

## 3. Selecting portfolio based on chosen level of risk

## 4. Measuring uncertainty in your strategy

If you had picked a portfolio based on the same criteria 20 years ago, how well would it have done? How certain or uncertain can you be that your strategy is the right one?