# Use Cases

This is a brief overview of how a user will interact with the tool and how this ties in to the various components defined above:

### Building a list of portfolios (asset allocation models)
The tab 'Portfolios' contains various inputs that the user can update to construct a list of different portfolios. Users
can update the initial investment amount, the time period of investment, the weights of various stocks/bonds in their
portfolios and the portfolio re-balancing frequency. Users can also visualize the pre-loaded asset data in order to help them decide what portfolios to test.

### Deciding on a risk and return measures
The risk and return measures used in the calculations can be experimented with. Users can select a Risk measure (probability of return below a threshold or standard deviation of returns) and Return measure (change in log value or change in percentage). Additional options in this page include a threshold for the rate of return, a frequency at which to measure return and if to use annualized measures of risk and return.

### Graphing
Once all the inputs are configured, the Risk-return tab of the UI shows a graph of all the portfolios. Each portfolio
is a single point and represents the risk/return over the time period selected in the portfolio configuration tab.

### Seeing how choice of risk measure affects asset allocation decisions
The user can change the risk/return measures using the inputs on the page and re-render the graph.

### Seeing how well past risk and returns predict future risk and returns
The user can go back to the previous tab and modify their set of portfolios and restrict the data source to a certain time period in the past. This allows them to compare (for example) the results if they had run the same query 20 years ago to the results today, and gives a sense of how uncertain the risk and reward levels shown by our tool are.

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
        
   ### Tab 4: Dataset visualization:
      - Allows user to visualize the raw investment class data.

![Interaction diagram](https://raw.githubusercontent.com/viv-r/asset-allocation/master/doc/frontend.png)

## Backend components:
   ### Data loader:
     - Description:
       - Loads the CSV data files into the app.
       - Pre-processes and cleans the raw data.
     - Inputs:
       - CSV files
     - Outputs:
       - Data frame for each investment class
   ### Risk and reward calculator:
     - Description:
        - Calculates number of shares of each investment class based on user input from the frontend.
        - Combines data frames for different investment classes into a single portfolio.
        - Calculates risk and reward on the portfolio over the given time period.
     - Inputs: Data frames for individual investment classes
     - Outputs: Risk and reward values
   ### Graphing function:
     - Description:
        - Bundles many portfolios together.
        - Calculates the same measure of risk and reward on each portfolio.
        - Exports a set of points to be graphed.
     - Inputs: Set of portfolios and graph parameters
     - Outputs: Set of points to be graphed
   ### User input - backend translator:
     - Description:
        - Translates user input into data frames, then calls graphing function to send data back to frontend.
        - Flow: Frontend --> backend --> frontend
     - Inputs: User-defined portfolios and parameters
     - Outputs: Set of points to be graphed

![Interaction diagram](https://raw.githubusercontent.com/viv-r/asset-allocation/master/doc/backend.png)
