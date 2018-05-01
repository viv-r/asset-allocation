# COMPONENTS

## Database containing data of stock, bonds, inflation and other market data sources.
## Frontend components:
   ### Inputs:
        - Risk measure selection.
        - Asset allocation model selection (list of portfolios)
        - Time period selection.
   ### Graphs
        - Plot of risk vs reward.
## Backend components:
   ### Data processing and setup:
     - Description:
       - Populates the DB with data from multiple CSV files.
       - Pre-processing and cleaning the raw data.
     - Inputs:
       - CSV files
     - Outpus:
       - None
   ### Data loader:
     - Description:
       - Opens a connection to the database.
       - Constructs a query to fetch the required data.
     - Inputs: Fields to fetch from the data (time period, stock/bond name, etc.)
     - Outputs: Rows from the DB
   ### A function calculate Risk/Reward values:
     - Description:
        - Call the data loader component.
        - Calculates the output.
     - Inputs: the user selection from the frontend
     - Outputs: List of data points to be plotted.

# Use Case Scenario

This is a brief overview of how a user will interact with the tool and how this ties in to the various components defined above:

### Deciding on a risk measure 
This is where the users interact with the first frontend component "Risk measure selection". A list of different risk measure models with a brief description of each will be available to users, who can then select one of these.  

### Selecting a list of portfolio (asset allocation models) for the chosen risk measure
Users interact with the second frontend component "Asset allocation model selection" where from a list of different portfolios, they can select which ones they wish to compare.

### Selecting a time period to view returns and risk 
Here the users interact with the third frontend component where they selects the time period (in years) over which they wish to see returns v/s risk for the preselected combinations of risk measure and portfolios. 

### Seeing how choice of risk measure affects asset allocation decisions
In the background, the user inputs will interact with all the backend components, returning a list of values to the frontend graph component which presents a plot of risk v/s reward to the user.


## 1. Risk-reward tradeoff analysis

Compare levels of risk and reward in different portfolios. Allow user to select various time horizons and measures of risk.

### 1a. Measures of risk

Built-in calculator for different methods of measuring risk and volatility in a stock portfolio
- Difference between risk and volatility

## 2. Probabilistic model of future performance based on past

Time-series / probabilistic model. Say you want to invest for a 20-year timeline. How well do past return and risk measures predict the next 20 years of returns?

Investment companies always tell us "past performance is no guarantee of future results". Can we quantify how uncertain it is?
