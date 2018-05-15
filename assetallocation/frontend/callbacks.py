
import riskreturn_graph
from assetallocation.generate_portfolios import get_graph_data
from dash.dependencies import Input, Output


def attach_callbacks(app):
    @app.callback(
        Output(component_id='riskreturn_graph', component_property='figure'),
        [Input(component_id='timeperiod_input', component_property='value')]
    )
    def update_timeperiod(value):
        return riskreturn_graph.get_params(*get_graph_data(*value))
