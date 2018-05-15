import dash
import dash_core_components as dcc
import dash_html_components as html

from generate_portfolios import get_graph_data
from frontend import timeperiod_input
from frontend import riskreturn_graph

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Asset allocation'),
    riskreturn_graph.get_component(*get_graph_data()),
    timeperiod_input.get_component()
])


if __name__ == '__main__':
    app.run_server(debug=True)
