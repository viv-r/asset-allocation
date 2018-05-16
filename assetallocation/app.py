import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from generate_portfolios import get_graph_data
from frontend import timeperiod_input
from frontend import riskreturn_graph

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Asset allocation'),
    riskreturn_graph.get_component(*get_graph_data()),
    timeperiod_input.get_component()
])


@app.callback(
    Output(component_id='riskreturn_graph', component_property='figure'),
    [Input(component_id='timeperiod_input', component_property='value')]
)
def update_timeperiod(value):
    print(value)
    return riskreturn_graph.get_params(*get_graph_data(*value))


if __name__ == '__main__':
    app.run_server(debug=True)
