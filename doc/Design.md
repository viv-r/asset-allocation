# Use Cases

This is a brief overview of how a user will interact with the tool and how this ties in to the various components defined above:

### Building a list of portfolios (asset allocation models)
The tab 'Portfolios' contains various inputs that the user can update to construct a list of different portfolios. Users
can update the initial investment amount, the time period of investment, the weights of various stocks/bonds in their
portfolios and the portfolio re-balancing frequency.

### Deciding on a risk measure
This is where the users interact with the first frontend component 'Risk measure selection'. A list of different risk measure models with a brief description of each will be available to users, who can then select one of these.

### Selecting a time period to view returns and risk
Here the users interact with the third frontend component where they select the time period (in years) over which they wish to see returns vs. risk for the preselected combinations of risk measure and portfolios.

### Seeing how choice of risk measure affects asset allocation decisions
In the background, the user inputs will interact with all the backend components, returning a list of values to the frontend graph component which presents a plot of risk vs. reward to the user.

### Seeing how well past risk and returns predict future risk and returns
The user interacts with the third front-end component where they graph the relationship between risk and return, but restrict the data source to a certain time period in the past. This allows them to compare (for example) the results if they had run the same query 20 years ago to the results today, and gives a sense of how uncertain the risk and reward levels shown by our tool are.

# Overview
![Interaction diagram](https://raw.githubusercontent.com/viv-r/asset-allocation/master/doc/components_diagram.jpg)

# Components
## Frontend components:
   Short descriptions of what each risk measure does
   List of portfolios to display on the graph
   ### Tab 1: Introduction:
      - A dash markdown component showing the readme file.

   ### Tab 2: Portfolios:
      - A tab containing the configuration for each portfolio
        that the user wants to see on the risk-return plot.
      - Each group of inputs represents a portfolio
      - A portfolio has the following input components.
         - Portfolio name text input
         - The initial investment amount
         - Re-balancing time period
         - Start and end dates
         - A list of investment classes (assets)
      - Each investment class contains a single asset and it's weight in the portfolio.

   ### Tab 3: Risk return graph:
      - Inputs that specify the type of risk/reward metric to be
        used in calculating the co-ordinates of the data points
          - Measure of return: (log change or percent change)
          - Measure of risk: (probability or standard deviation)
          - Period of return to use for risk measure
          - Threshold rate of return
          - Frequency to measure return
          - If to use annualized return for risk/reward.
        - A plotly graph component showing the final plot.

![Interaction diagram](https://raw.githubusercontent.com/viv-r/asset-allocation/master/doc/fontend.jpg)

## Backend components:
   ### Data processing and setup:
     - Description:
       - Loads the csv data files into the app.
       - Pre-processing and cleaning the raw data.
     - Inputs:
       - CSV files
     - Outputs:
       - None
   ### Data loader:
     - Description:
       - Opens a connection to the database.
       - Constructs a query to fetch the required data.
     - Inputs: Fields to fetch from the data (time period, stock/bond name, etc.)
     - Outputs: Rows from the DB
   ### A function to calculate Risk/Reward values:
     - Description:
        - Call the data loader component.
        - Calculates the output.
     - Inputs: the user selection from the frontend
     - Outputs: List of data points to be plotted.
   ### Probabilistic model of future performance based on past:
     - Description:
        - Calculates output of risk/reward value function as if it had been run at many different times in the past.
     - Inputs: user selection from the front end
     - Outputs: a measure of how robust the risk/reward measures are over different time periods

![Interaction diagram](https://raw.githubusercontent.com/viv-r/asset-allocation/master/doc/backend.jpg)
